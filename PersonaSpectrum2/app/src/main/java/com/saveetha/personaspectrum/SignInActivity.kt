package com.saveetha.personaspectrum

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class SignInActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Set the content view to the sign-in layout
        setContentView(R.layout.activity_sign_in)

        val backArrow = findViewById<ImageView>(R.id.back_arrow)
        backArrow.setOnClickListener {
            finish()
        }

        val createAccount = findViewById<TextView>(R.id.create_account_text)
        createAccount.setOnClickListener {
            startActivity(Intent(this, CreateAccountActivity::class.java))
        }

        val forgotPassword = findViewById<TextView>(R.id.forgot_password_text)
        forgotPassword.setOnClickListener {
            startActivity(Intent(this, ForgotPasswordActivity::class.java))
        }

        val signInButton = findViewById<Button>(R.id.sign_in_button)
        signInButton.setOnClickListener {
            val emailOrUsername = findViewById<EditText>(R.id.email_username_input).text.toString()
            val password = findViewById<EditText>(R.id.password_input).text.toString()

            val loginRequest = LoginRequest(emailOrUsername, password)

            RetrofitClient.instance.loginUser(loginRequest)
                .enqueue(object : Callback<Token> {
                    override fun onResponse(call: Call<Token>, response: Response<Token>) {
                        if (response.isSuccessful) {
                            response.body()?.let { token ->
                                TokenManager.saveToken(this@SignInActivity, token.accessToken)
                                Toast.makeText(this@SignInActivity, "Login successful!", Toast.LENGTH_SHORT).show()
                                startActivity(Intent(this@SignInActivity, IntroActivity::class.java))
                                finish()
                            }
                        } else {
                            Toast.makeText(this@SignInActivity, "Login failed: ${response.message()}", Toast.LENGTH_SHORT).show()
                        }
                    }

                    override fun onFailure(call: Call<Token>, t: Throwable) {
                        Toast.makeText(this@SignInActivity, "Error: ${t.message}", Toast.LENGTH_SHORT).show()
                    }
                })
        }
    }
}
