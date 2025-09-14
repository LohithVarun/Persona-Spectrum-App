package com.saveetha.personaspectrum

import android.content.Intent
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class LoadingResultsActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_loading_results)

        // Use a handler to add a small delay for better UX
        Handler(Looper.getMainLooper()).postDelayed({
            fetchResults()
        }, 3000) // 3-second delay
    }

    private fun fetchResults() {
        val token = TokenManager.getToken(this)
        if (token == null) {
            Toast.makeText(this, "Authentication error. Please log in again.", Toast.LENGTH_LONG).show()
            // Redirect to login screen
            startActivity(Intent(this, LoginActivity::class.java))
            finish()
            return
        }

        RetrofitClient.instance.getLatestResult("Bearer $token")
            .enqueue(object : Callback<PersonalityResult> {
                override fun onResponse(call: Call<PersonalityResult>, response: Response<PersonalityResult>) {
                    if (response.isSuccessful) {
                        response.body()?.let {
                            val intent = Intent(this@LoadingResultsActivity, ResultsActivity::class.java)
                            intent.putExtra("personality_result", it)
                            startActivity(intent)
                            finish()
                        }
                    } else {
                        Toast.makeText(this@LoadingResultsActivity, "Failed to load results.", Toast.LENGTH_SHORT).show()
                    }
                }

                override fun onFailure(call: Call<PersonalityResult>, t: Throwable) {
                    Toast.makeText(this@LoadingResultsActivity, "Error: ${t.message}", Toast.LENGTH_SHORT).show()
                }
            })
    }
}
