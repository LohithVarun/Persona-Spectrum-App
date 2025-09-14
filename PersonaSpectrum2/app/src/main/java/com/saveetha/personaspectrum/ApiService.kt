package com.saveetha.personaspectrum

import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.Header
import retrofit2.http.POST

interface ApiService {
    @POST("/api/auth/register")
    fun registerUser(@Body user: UserCreate): Call<UserResponse>

    @POST("/api/auth/token")
    fun loginUser(@Body login: LoginRequest): Call<Token>

    @GET("/api/questions")
    fun getQuestions(@Header("Authorization") token: String): Call<List<Question>>

    @POST("/api/submit-assessment")
    fun submitAssessment(@Header("Authorization") token: String, @Body request: SubmitAnswersRequest): Call<PersonalityResult>

    @GET("/api/results/latest")
    fun getLatestResult(@Header("Authorization") token: String): Call<PersonalityResult>

    @GET("/api/users/me")
    fun getCurrentUser(@Header("Authorization") token: String): Call<UserResponse>

    @GET("/api/results/history")
    fun getAssessmentHistory(@Header("Authorization") token: String): Call<List<PersonalityResult>>
}
