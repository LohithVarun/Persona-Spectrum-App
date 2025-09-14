package com.saveetha.personaspectrum

import android.content.Context
import android.content.SharedPreferences

object TokenManager {
    private const val PREF_NAME = "PersonaSpectrumPrefs"
    private const val KEY_ACCESS_TOKEN = "access_token"

    private fun getPrefs(context: Context): SharedPreferences {
        return context.getSharedPreferences(PREF_NAME, Context.MODE_PRIVATE)
    }

    fun saveToken(context: Context, token: String) {
        val editor = getPrefs(context).edit()
        editor.putString(KEY_ACCESS_TOKEN, token)
        editor.apply()
    }

    fun getToken(context: Context): String? {
        return getPrefs(context).getString(KEY_ACCESS_TOKEN, null)
    }

    fun clearToken(context: Context) {
        val editor = getPrefs(context).edit()
        editor.remove(KEY_ACCESS_TOKEN)
        editor.apply()
    }
}
