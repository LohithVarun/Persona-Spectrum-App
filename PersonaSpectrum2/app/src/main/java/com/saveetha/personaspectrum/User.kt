package com.saveetha.personaspectrum

import java.io.Serializable

data class User(
    val id: Int,
    val email: String,
    val username: String
) : Serializable
