package com.saveetha.personaspectrum

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.LinearLayout
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.bottomnavigation.BottomNavigationView
import java.text.SimpleDateFormat
import java.util.Locale
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class ProfileActivity : AppCompatActivity() {

    private lateinit var usernameTextView: TextView
    private lateinit var emailTextView: TextView
    private lateinit var assessmentHistoryContainer: LinearLayout
    private lateinit var logoutButton: Button
    private lateinit var bottomNavigationView: BottomNavigationView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_profile)

        usernameTextView = findViewById(R.id.username_text)
        emailTextView = findViewById(R.id.email_text)
        assessmentHistoryContainer = findViewById(R.id.assessment_history_container)
        logoutButton = findViewById(R.id.logout_button)
        bottomNavigationView = findViewById(R.id.bottom_navigation)

        fetchUserProfile()
        fetchAssessmentHistory()

        logoutButton.setOnClickListener {
            TokenManager.clearToken(this)
            val intent = Intent(this, LoginActivity::class.java)
            intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
            startActivity(intent)
        }

        bottomNavigationView.setOnNavigationItemSelectedListener { item ->
            when (item.itemId) {
                R.id.nav_results -> {
                    fetchAndNavigate(ResultsActivity::class.java)
                    true
                }
                R.id.nav_recommendations -> {
                    fetchAndNavigate(RecommendationsActivity::class.java)
                    true
                }
                R.id.nav_profile -> {
                    // Already on the profile screen
                    true
                }
                else -> false
            }
        }

        val reassessLink = findViewById<TextView>(R.id.reassess_link)
        reassessLink.setOnClickListener {
            val intent = Intent(this, QuestionActivity::class.java)
            // Pass a flag to indicate this is a re-assessment
            intent.putExtra("is_reassessment", true)
            startActivity(intent)
        }
    }

    // Helper function to fetch the latest result and navigate
    private fun <T> fetchAndNavigate(activityClass: Class<T>) {
        val token = TokenManager.getToken(this) ?: return
        RetrofitClient.instance.getLatestResult("Bearer $token").enqueue(object : Callback<PersonalityResult> {
            override fun onResponse(call: Call<PersonalityResult>, response: Response<PersonalityResult>) {
                if (response.isSuccessful) {
                    val intent = Intent(this@ProfileActivity, activityClass)
                    intent.putExtra("personality_result", response.body())
                    startActivity(intent)
                } else {
                    Toast.makeText(this@ProfileActivity, "Could not load latest results.", Toast.LENGTH_SHORT).show()
                }
            }
            override fun onFailure(call: Call<PersonalityResult>, t: Throwable) {
                Toast.makeText(this@ProfileActivity, "Error: ${t.message}", Toast.LENGTH_SHORT).show()
            }
        })
    }

    private fun fetchUserProfile() {
        val token = TokenManager.getToken(this)
        if (token == null) {
            // Handle error
            return
        }

        RetrofitClient.instance.getCurrentUser("Bearer $token").enqueue(object : Callback<UserResponse> {
            override fun onResponse(call: Call<UserResponse>, response: Response<UserResponse>) {
                if (response.isSuccessful) {
                    response.body()?.let {
                        usernameTextView.text = it.username
                        emailTextView.text = it.email
                    }
                } else {
                    Toast.makeText(this@ProfileActivity, "Failed to fetch user profile", Toast.LENGTH_SHORT).show()
                }
            }

            override fun onFailure(call: Call<UserResponse>, t: Throwable) {
                Toast.makeText(this@ProfileActivity, "Error: ${t.message}", Toast.LENGTH_SHORT).show()
            }
        })
    }

    private fun fetchAssessmentHistory() {
        val token = TokenManager.getToken(this)
        if (token == null) {
            // Handle error
            return
        }

        RetrofitClient.instance.getAssessmentHistory("Bearer $token").enqueue(object : Callback<List<PersonalityResult>> {
            override fun onResponse(call: Call<List<PersonalityResult>>, response: Response<List<PersonalityResult>>) {
                if (response.isSuccessful) {
                    response.body()?.let { history ->
                        displayAssessmentHistory(history)
                    }
                } else {
                    Toast.makeText(this@ProfileActivity, "Failed to fetch assessment history", Toast.LENGTH_SHORT).show()
                }
            }

            override fun onFailure(call: Call<List<PersonalityResult>>, t: Throwable) {
                Toast.makeText(this@ProfileActivity, "Error: ${t.message}", Toast.LENGTH_SHORT).show()
            }
        })
    }

    private fun displayAssessmentHistory(history: List<PersonalityResult>) {
        assessmentHistoryContainer.removeAllViews()
        val formatter = SimpleDateFormat("yyyy-MM-dd", Locale.getDefault())
        for (result in history) {
            val historyView = layoutInflater.inflate(R.layout.item_assessment_history, assessmentHistoryContainer, false)
            val historyText = historyView.findViewById<TextView>(R.id.history_text)
            // Format the date and name
            val date = formatter.format(result.timestamp)
            historyText.text = "$date - ${result.name}"
            assessmentHistoryContainer.addView(historyView)
        }
    }
}
