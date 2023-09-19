This project is a Flask web application that uses the OpenAI GPT-3 API to generate a list of top-rated movies on IMDb based on a user-provided genre keyword.
Here's a brief explanation of the project:

**Objective:**
The project aims to create a simple web interface where users can enter their favorite movie genre, and the application will use OpenAI's GPT-3 model to 
generate a list of top-rated movies in that genre.

**Key Components:**

1. **Flask Web Application:**
   - The project is built using the Flask web framework, which allows for the creation of web applications in Python.
   - Flask handles routing, form submissions, and rendering HTML templates.

2. **OpenAI GPT-3 Integration:**
   - The application integrates with the OpenAI GPT-3 API to generate movie recommendations.
   - The OpenAI API key is configured within the Flask application to enable API access.

3. **User Interaction:**
   - Users interact with the application through a web form.
   - They enter their favorite movie genre in an input field and submit the form.

4. **Processing User Input:**
   - When the form is submitted, the Flask application captures the user's input (the movie genre) from the form data.
   - It constructs a prompt for the GPT-3 model using the entered genre.

5. **Request to OpenAI API:**
   - The application sends a request to the OpenAI GPT-3 API, providing the constructed prompt.
   - It specifies the GPT-3 model to use (`'text-davinci-003'`), sets a maximum token limit for the response (`max_tokens`), and adjusts the
   - "temperature" to control the randomness of the response.

6. **Displaying Movie Recommendations:**
   - After receiving the response from the GPT-3 API, the application extracts the generated movie keywords.
   - It then renders an HTML template that displays the list of recommended movies based on the user's input genre.

**How It Works:**
   - Users access the web application and are presented with a form.
   - They enter their favorite movie genre and click the "Generate Movies" button.
   - The application sends the genre as a prompt to the GPT-3 model.
   - GPT-3 generates a list of movie-related keywords based on the genre.
   - The application displays the generated movie keywords on the web page.

**Use Cases:**
   - This project demonstrates a simple use case of using AI to generate movie recommendations based on user input.
   - It can be expanded and improved to include more advanced features like movie descriptions, IMDb ratings, or even links to watch the recommended movies.

Overall, this project showcases how to create a basic web application that leverages AI to provide personalized recommendations in response to user
queries, making it suitable for applications involving content recommendations and natural language generation.
