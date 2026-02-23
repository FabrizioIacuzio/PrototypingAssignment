import streamlit as st
from groq import Groq
from gtts import gTTS
import os

# Approximate words per minute for spoken audio
WORDS_PER_MINUTE = 140

def process_reports_and_generate_audio(selected_reports, duration_minutes=3):
    """
    Generate an AI briefing script and audio from selected financial reports.
    
    Args:
        selected_reports: DataFrame with Sender, Subject, Content columns
        duration_minutes: Target length of the briefing in minutes (1, 3, or 5)
    
    Returns:
        tuple: (script_text, audio_file_path)
    """
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

    context = ""
    for index, row in selected_reports.iterrows():
        context += f"Source: {row['Sender']} - Subject: {row['Subject']} - Content: {row['Content']}\n\n"

    target_word_count = duration_minutes * WORDS_PER_MINUTE

    prompt = f"""
    You are a professional financial analyst assistant.
    Analyze the following reports and create a single, cohesive morning briefing script.

    CRITICAL: The script must be approximately {target_word_count} words in length (suitable for {duration_minutes} minute(s) of spoken audio at normal pace).
    Do not exceed this length. Be concise and prioritize the most important points.

    Instructions:
    - Group similar topics together (Clustering).
    - Use a professional, engaging tone suitable for an audio podcast.
    - Start with: 'Good morning, here is your AI financial briefing.'
    - End with: 'Stay informed and have a productive day.'
    - Focus on the most material information; omit minor details if needed to stay within the target length.

    Reports to analyze:
    {context}
    """

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile", #
            temperature=0.7,
        )
        script = chat_completion.choices[0].message.content

        
        audio_path = "briefing.mp3"
        
        if os.path.exists(audio_path):
            os.remove(audio_path)
            
        tts = gTTS(text=script, lang='en')
        tts.save(audio_path)

        return script, audio_path

    except Exception as e:
        
        raise Exception(f"Error in Groq/gTTS pipeline: {str(e)}")