package com.saveetha.personaspectrum

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class WelcomeActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_welcome)

        val signInButton: Button = findViewById(R.id.sign_in_button)
        val createAccountButton: Button = findViewById(R.id.create_account_button)
        val guestButton: TextView = findViewById(R.id.guest_button)

        signInButton.setOnClickListener {
            // TODO: Implement Sign In functionality
        }

        createAccountButton.setOnClickListener {
            // TODO: Implement Create Account functionality
        }

        guestButton.setOnClickListener {
            // TODO: Implement Continue as Guest functionality
        }
    }
}
