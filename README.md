# remesh_takehome
Remesh Take Home project-- Twitter Data Visualization 

![Screen Shot 2021-05-07 at 8 14 43 PM](https://user-images.githubusercontent.com/25694681/117519287-f665d980-af70-11eb-8d32-1c8ed544eb85.png)

This is my app for the data visualization take home project. For this project, I used Plotly Express and Dash to create an interactive visualization. 

Please follow the instructions below: 

1. Download the project files and ensure data.json and data_visualization.py are in the same directory 
2. Open data_visualization.py in your favorite IDE or terminal/command line, ensuring data.json is in the same directory
3. Ensure you have all of the relevant modules imported: json, pathlib, pandas, plotly.express, and dash
4. Once you have all of the modules imported, run data_visualization.py
5. When you run data_visualization.py, the program will output this with your local host in place of your_local_host_ip_and_port: 

"
Dash is running on http:// your_local_host_ip_and_port

 * Serving Flask app "data_visualization" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 "

6. Click the link to your_local_host_ip_and_port that was outputted by data_visualization.py or copy and paste your local host and port into a web browser
7. Now you will be able to see the data visualizations on your local host and interact with the visualizations within your browser 


How I define engagement- 
In this project, I define engagement as the total number of likes and retweets for a tweet. I created a score called engagement score which is the number of retweets for a tweet + the number of likes for a tweet. In addition, the tweet score = length of the tweet + number of hashtags. With this in mind my visualizations revolve around showcasing the relationships between tweet likes and engagement, in addtion to the number of hashtags and engagement. I chose this measure of engagement because both a tweet's number of likes and number of retweets are crucial in seeing how people interacted with a tweet. From the number of likes and retweets a tweet has we see how many people interacted with the post.

Thank you for your time and if you have any questions feel free to reach out!
