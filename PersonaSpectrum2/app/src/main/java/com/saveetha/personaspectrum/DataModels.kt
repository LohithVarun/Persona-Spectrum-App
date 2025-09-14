package com.saveetha.personaspectrum

import com.google.gson.annotations.SerializedName
import java.io.Serializable
import java.util.Date

// --- Models for fetching questions ---
data class Option(
    val value: Int,
    val text: String
) : Serializable

data class Question(
    val id: Int,
    @SerializedName("question_number")
    val questionNumber: Int,
    val text: String,
    val category: String,
    @SerializedName("options_data")
    val options: List<Option>
) : Serializable

// --- Models for submitting answers ---
data class Answer(
    @SerializedName("question_id")
    val questionId: Int,
    @SerializedName("selected_value")
    val selectedValue: Int
)

data class SubmitAnswersRequest(
    @SerializedName("assessment_name")
    val assessmentName: String = "Initial Assessment",
    val answers: List<Answer>
)

// --- Models for displaying results ---
data class Recommendation(
    val dimension: String,
    val trait: String,
    val advice: String,
    @SerializedName("app_suggestion")
    val appSuggestion: String?
) : Serializable

data class PersonalityResult(
    val id: Int,
    @SerializedName("user_id")
    val userId: Int,
    val timestamp: Date,
    val name: String?,
    @SerializedName("summary_statement")
    val summaryStatement: String?,
    val scores: Map<String, Float>,
    val recommendations: List<Recommendation>
) : Serializable

// --- User Auth Models ---
data class LoginRequest(
    val username: String, // Can be email or username
    val password: String
)

data class Token(
    @SerializedName("access_token")
    val accessToken: String,
    @SerializedName("token_type")
    val tokenType: String
)

data class UserCreate(
    val email: String,
    val username: String,
    val password: String
)

data class UserResponse(
    val id: Int,
    val email: String,
    val username: String
) : Serializable


