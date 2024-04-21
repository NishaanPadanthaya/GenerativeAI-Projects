This user story generator is designed to assist in Agile project planning for web applications or apps.
A user story is a concise, informal description of a feature or functionality from an end user's perspective
User stories are typically written collaboratively by the development team and stakeholders, and they serve as the basis for planning, development,
and testing activities throughout the Agile development process.

Now here we are using the help of AI to generate the user stories,acceptence criteria and user story points.
Here's how it works:

1. **Setup and Configuration**: The script first imports necessary libraries like dotenv for environment variables, google.generativeai for accessing AI models, os
    for operating system functionalities, streamlit for creating web apps, and PIL from the Python Imaging Library for image processing.

3. **API Configuration**: It configures the access to the generative AI model provided by Google using an API key stored in the environment variables.

4. **Generative Model Initialization**: It initializes the generative model for content generation. In this case, it seems to be a model named "gemini-pro-vision" provided by Google.

5. **User Input Handling**: The Streamlit app interface allows users to input the number of user stories needed (num_workers) and the deadline for completion (num_days).
   Users can also upload a design or workflow image relevant to the project.

7. **Content Generation**: Upon uploading the image and providing project details, the script generates a prompt based on the input parameters and the uploaded image.
   This prompt includes instructions for generating user stories relevant to Agile project planning for the given project.

9. **Displaying Generated User Stories**: Finally, the generated user stories are displayed on the Streamlit web app interface for the user to review.

Overall, this script utilizes gemini-pro-vision to streamline the process of creating Agile project plans by automatically generating descriptive user stories based on provided project details 
and uploaded images of designs or workflows.
