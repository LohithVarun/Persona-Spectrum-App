package com.saveetha.personaspectrum

import android.content.Intent
import android.os.Bundle
import android.util.Patterns
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import android.widget.TextView
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class CreateAccountActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_create_account)

        val backArrow = findViewById<ImageView>(R.id.back_arrow)
        backArrow.setOnClickListener {
            finish()
        }

        val signInLink = findViewById<TextView>(R.id.sign_in_link)
        signInLink.setOnClickListener {
            startActivity(Intent(this, LoginActivity::class.java))
        }

        val createAccountButton = findViewById<Button>(R.id.create_account_button)
        createAccountButton.setOnClickListener {
            val emailInput = findViewById<EditText>(R.id.email_username_input)
            val passwordInput = findViewById<EditText>(R.id.password_input)
            val confirmPasswordInput = findViewById<EditText>(R.id.confirm_password_input)

            val email = emailInput.text.toString().trim()
            val password = passwordInput.text.toString()
            val confirmPassword = confirmPasswordInput.text.toString()

            if (!isValidEmail(email)) {
                emailInput.error = "Enter a valid email address"
                return@setOnClickListener
            }

            if (password.length < 8) {
                passwordInput.error = "Password must be at least 8 characters"
                return@setOnClickListener
            }

            if (password != confirmPassword) {
                confirmPasswordInput.error = "Passwords do not match"
                return@setOnClickListener
            }

            // Assuming username is the same as email for simplicity
            val user = UserCreate(email, email, password)

            RetrofitClient.instance.registerUser(user)
                .enqueue(object : Callback<UserResponse> {
                    override fun onResponse(call: Call<UserResponse>, response: Response<UserResponse>) {
                        if (response.isSuccessful) {
                            Toast.makeText(this@CreateAccountActivity, "Account created successfully", Toast.LENGTH_SHORT).show()
                            startActivity(Intent(this@CreateAccountActivity, SignInActivity::class.java))
                        } else {
                            Toast.makeText(this@CreateAccountActivity, "Registration failed: ${response.errorBody()?.string()}", Toast.LENGTH_LONG).show()
                        }
                    }

                    override fun onFailure(call: Call<UserResponse>, t: Throwable) {
                        Toast.makeText(this@CreateAccountActivity, "Error: ${t.message}", Toast.LENGTH_SHORT).show()
                    }
                })
        }
    }

    private fun isValidEmail(email: String): Boolean {
        return email.isNotEmpty() && Patterns.EMAIL_ADDRESS.matcher(email).matches()
    }
}
