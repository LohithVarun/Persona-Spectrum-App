package com.saveetha.personaspectrum

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.LinearLayout
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class ResultsActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_results)

        val result = intent.getSerializableExtra("personality_result") as? PersonalityResult

        if (result == null) {
            finish()
            return
        }

        val summaryTextView = findViewById<TextView>(R.id.summary_statement_text)
        val scoresContainer = findViewById<LinearLayout>(R.id.scores_container)
        val recommendationsButton = findViewById<Button>(R.id.recommendations_button)

        summaryTextView.text = result.summaryStatement ?: "Here is your personality breakdown."

        displayScores(scoresContainer, result.scores)

        recommendationsButton.setOnClickListener {
            val intent = Intent(this, RecommendationsActivity::class.java)
            intent.putExtra("personality_result", result)
            startActivity(intent)
        }
    }

    private fun displayScores(container: LinearLayout, scores: Map<String, Float>) {
        container.removeAllViews()

        val dimensionMap = mapOf(
            "Introvert_Extrovert" to "Energy",
            "Sensing_Intuition" to "Information",
            "Thinking_Feeling" to "Decisions",
            "Judging_Perceiving" to "Lifestyle"
        )

        for ((dimension, score) in scores) {
            val scoreView = layoutInflater.inflate(R.layout.item_score, container, false)
            val title = scoreView.findViewById<TextView>(R.id.score_title)
            val description = scoreView.findViewById<TextView>(R.id.score_description)

            val (trait1, trait2) = dimension.split('_')
            val dominantTrait = if (score < 0) trait1 else trait2
            val displayName = dimensionMap[dimension] ?: dimension

            title.text = "$displayName ($trait1 vs. $trait2)"
            description.text = "Your dominant trait is $dominantTrait with a score of ${String.format("%.1f", Math.abs(score))}%"

            container.addView(scoreView)
        }
    }
}