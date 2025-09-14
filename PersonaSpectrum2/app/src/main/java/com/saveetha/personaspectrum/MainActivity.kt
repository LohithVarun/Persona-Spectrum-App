package com.saveetha.personaspectrum
import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.saveetha.personaspectrum.CreateAccountActivity
import com.saveetha.personaspectrum.HomeActivity
import com.saveetha.personaspectrum.LoginActivity
import com.saveetha.personaspectrum.R


class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val btnSignIn = findViewById<Button>(R.id.btnSignIn)
        val btnCreateAccount = findViewById<Button>(R.id.btnCreateAccount)
        val tvGuest = findViewById<TextView>(R.id.tvGuest)

        btnSignIn.setOnClickListener {
            startActivity(Intent(this, SignInActivity::class.java))
        }

        btnCreateAccount.setOnClickListener {
            startActivity(Intent(this, CreateAccountActivity::class.java))
        }

        tvGuest.setOnClickListener {
            startActivity(Intent(this, IntroActivity::class.java))
        }
    }
}