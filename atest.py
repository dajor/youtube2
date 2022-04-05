"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

mytext = """Creating and adapting a table in Doc², before a table can be taught automatically in Doc², then read out, the function must first be activated. For this purpose, Modules, Tables, Extraction must be selected under Settings. Subsequently, this function is now active. If a table is to be read out of the document using Square, the said document must first be uploaded and processed there. After opening the document and possibly checking the header data, the table icon must be clicked at the very bottom under Articles. After opening the document and possibly checking the header data, click on the table icon at the bottom of the article. This will take us to the table view. On the left side there is a small overview of all pages of the document. You can also navigate between the pages using this overview. The current page has a purple border. In the middle there is a display of the current page of the document, while to the right the extracted data is displayed. To create a new table or edit an existing one, the training mode must be activated. This gives us several processing options. On the one hand, we can search in the display and try to have the system automatically recognize a table. If the table is to be taught manually, the Edit button must be activated and then the desired table must be marked. With the button etc. marks are added, which mark the different columns. Afterwards, the Save icon is clicked and the recognized data is displayed on the right side of the table. Above the table there are various functions. These are from left to right undo changes. Advanced settings of the. Can set the number of time we will delete the data. Block the extraction of the table for this supplier enable custom columns add custom column rows edit data mode enabled This mode is needed when specific part data within the fields should be read and special rules when manually add regex rules. To complete the table, the columns must first be assigned accordingly here. If columns are superfluous or cannot be extracted, they can be deleted. Similarly, superfluous rows can be removed by clicking on the X. Under the three dots next to the column names you will find the Delete button as well as the Group lines icon Lines Pin is used to indicate in the system when a new line begins. It is recommended to use the position House number or Sum here. If the content of the table is wrong or could not be read out immediately, the corresponding field in the table must be selected by a click and then in the document the corresponding content must also be selected with a double click or a mark. Let's look at the rows now, as the working mode is closer, this activated can be for extra audible column all that have a blue heading, additional data for future automatic extraction deposited, if an additional column is necessary, it can be added here. To extract the data, the corresponding field must first be clicked and then the desired information must be selected on the document. Once all the required data has been stored in the table, the table must be saved and then exported. With the export, the newly created rules are saved and are usually applied immediately when uploading the same data type."""

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=mytext)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",name="en-US-Wavenet-E", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
