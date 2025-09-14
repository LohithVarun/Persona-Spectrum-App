package com.saveetha.personaspectrum

import android.content.Intent
import android.os.Bundle
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class QuestionActivity : AppCompatActivity() {

    private lateinit var progressBar: ProgressBar
    private lateinit var questionCounter: TextView
    private lateinit var questionText: TextView
    private lateinit var optionsRadioGroup: RadioGroup
    private lateinit var previousButton: Button
    private lateinit var nextButton: Button

    private var questions: List<Question> = emptyList()
    private var currentQuestionIndex = 0
    private val userAnswers = mutableMapOf<Int, Int>() // questionId to selectedValue

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_question)

        progressBar = findViewById(R.id.progress_bar)
        questionCounter = findViewById(R.id.question_counter)
        questionText = findViewById(R.id.question_text)
        optionsRadioGroup = findViewById(R.id.options_radio_group)
        previousButton = findViewById(R.id.previous_button)
        nextButton = findViewById(R.id.next_button)

        fetchQuestions()

        previousButton.setOnClickListener {
            saveCurrentAnswer()
            if (currentQuestionIndex > 0) {
                currentQuestionIndex--
                displayQuestion()
            }
        }

        nextButton.setOnClickListener {
            // Before proceeding, ensure an answer is selected for the current question
            if (optionsRadioGroup.checkedRadioButtonId == -1) {
                Toast.makeText(this, "Please select an option.", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            saveCurrentAnswer()
            if (currentQuestionIndex < questions.size - 1) {
                currentQuestionIndex++
                displayQuestion()
            } else {
                submitAnswers()
            }
        }
    }

    private fun fetchQuestions() {
        val token = TokenManager.getToken(this)
        if (token == null) {
            Toast.makeText(this, "Authentication error.", Toast.LENGTH_LONG).show()
            finish()
            return
        }

        RetrofitClient.instance.getQuestions("Bearer $token")
            .enqueue(object : Callback<List<Question>> {
                override fun onResponse(call: Call<List<Question>>, response: Response<List<Question>>) {
                    if (response.isSuccessful) {
                        response.body()?.let {
                            questions = it.sortedBy { q -> q.questionNumber }
                            progressBar.max = questions.size
                            if (questions.isNotEmpty()) {
                                displayQuestion()
                            }
                        }
                    } else {
                        Toast.makeText(this@QuestionActivity, "Failed to load questions.", Toast.LENGTH_SHORT).show()
                    }
                }

                override fun onFailure(call: Call<List<Question>>, t: Throwable) {
                    Toast.makeText(this@QuestionActivity, "Error: ${t.message}", Toast.LENGTH_SHORT).show()
                }
            })
    }

    private fun displayQuestion() {
        if (questions.isEmpty() || currentQuestionIndex !in questions.indices) return

        val question = questions[currentQuestionIndex]
        progressBar.progress = currentQuestionIndex + 1
        questionCounter.text = "Question ${currentQuestionIndex + 1} of ${questions.size}"
        questionText.text = question.text

        optionsRadioGroup.removeAllViews()
        // Reverse the order of options so "Strongly Agree" is on top
        question.options.reversed().forEach { option ->
            val radioButton = RadioButton(this).apply {
                text = option.text
                id = option.value // Use option value as the ID
                textSize = 18f
                // Add some vertical margin to space out the buttons
                val layoutParams = RadioGroup.LayoutParams(
                    RadioGroup.LayoutParams.MATCH_PARENT,
                    RadioGroup.LayoutParams.WRAP_CONTENT
                )
                layoutParams.setMargins(0, 16, 0, 16)
                this.layoutParams = layoutParams
            }
            optionsRadioGroup.addView(radioButton)
        }

        // Restore the saved answer for this question, if it exists
        val savedAnswerValue = userAnswers[question.id]
        if (savedAnswerValue != null) {
            optionsRadioGroup.check(savedAnswerValue)
        } else {
            optionsRadioGroup.clearCheck()
        }

        previousButton.isEnabled = currentQuestionIndex > 0
        nextButton.text = if (currentQuestionIndex == questions.size - 1) "Submit" else "Next"
    }

    private fun saveCurrentAnswer() {
        if (questions.isNotEmpty() && currentQuestionIndex in questions.indices) {
            val questionId = questions[currentQuestionIndex].id
            val selectedRadioButtonId = optionsRadioGroup.checkedRadioButtonId
            if (selectedRadioButtonId != -1) {
                userAnswers[questionId] = selectedRadioButtonId
            }
        }
    }

    private fun submitAnswers() {
        val token = TokenManager.getToken(this)
        if (token == null) {
            Toast.makeText(this, "Authentication error.", Toast.LENGTH_LONG).show()
            return
        }

        // Create the list of Answer objects from our saved answers
        val answers = userAnswers.map { (questionId, selectedValue) ->
            Answer(questionId = questionId, selectedValue = selectedValue)
        }

        val request = SubmitAnswersRequest(answers = answers)

        RetrofitClient.instance.submitAssessment("Bearer $token", request)
            .enqueue(object : Callback<PersonalityResult> {
                override fun onResponse(call: Call<PersonalityResult>, response: Response<PersonalityResult>) {
                    if (response.isSuccessful) {
                        response.body()?.let { result ->
                            val intent = Intent(this@QuestionActivity, ResultsActivity::class.java)
                            intent.putExtra("personality_result", result)
                            startActivity(intent)
                            finish() // Finish this activity so the user can't go back to it
                        }
                    } else {
                        Toast.makeText(this@QuestionActivity, "Failed to submit answers.", Toast.LENGTH_SHORT).show()
                    }
                }

                override fun onFailure(call: Call<PersonalityResult>, t: Throwable) {
                    Toast.makeText(this@QuestionActivity, "Error: ${t.message}", Toast.LENGTH_SHORT).show()
                }
            })
    }
}