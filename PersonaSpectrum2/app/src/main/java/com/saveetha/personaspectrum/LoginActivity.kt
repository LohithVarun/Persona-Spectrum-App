package com.saveetha.personaspectrum

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class LoginActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        val signInButton = findViewById<Button>(R.id.sign_in_button)
        signInButton.setOnClickListener {
            startActivity(Intent(this, IntroActivity::class.java))
        }
    }
}
