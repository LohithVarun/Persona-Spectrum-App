package com.saveetha.personaspectrum

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.LinearLayout
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class RecommendationsActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_recommendations)

        val result = intent.getSerializableExtra("personality_result") as? PersonalityResult
        val recommendationsContainer = findViewById<LinearLayout>(R.id.recommendations_container)
        val doneButton = findViewById<Button>(R.id.done_button)

        if (result == null) {
            finish()
            return
        }

        displayRecommendations(recommendationsContainer, result.recommendations)

        doneButton.setOnClickListener {
            // Navigate back to the main screen, clearing the task stack
            val intent = Intent(this, MainActivity::class.java)
            intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
            startActivity(intent)
        }
    }

    private fun displayRecommendations(container: LinearLayout, recommendations: List<Recommendation>) {
        container.removeAllViews() // Clear previous views

        if (recommendations.isEmpty()) {
            val noRecsView = TextView(this)
            noRecsView.text = "Your personality profile is well-balanced. No specific development recommendations at this time."
            container.addView(noRecsView)
            return
        }

        for (rec in recommendations) {
            val recommendationView = layoutInflater.inflate(R.layout.item_recommendation, container, false)
            val title = recommendationView.findViewById<TextView>(R.id.recommendation_title)
            val description = recommendationView.findViewById<TextView>(R.id.recommendation_description)
            val appSuggestion = recommendationView.findViewById<TextView>(R.id.recommendation_app_suggestion)

            title.text = "For Your ${rec.trait} Trait:"
            description.text = rec.advice
            appSuggestion.text = rec.appSuggestion ?: ""

            container.addView(recommendationView)
        }
    }
}