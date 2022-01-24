# Emotion_Detection
<div id="top"></div>

[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mstatt/Emotion_Detection">
    <img src="assets/falcons-logo2.png" alt="Logo" >
  </a>

  <h3 align="center">
Emotion_Detection</h3>

  <p align="center">
    A light repo to get up and running with Emotion Detection using streamlit on your local machine.
    <br />
    <br />
    <a href="https://www.youtube.com/watch?v=AWB2cEKcME0">View Demo</a>
    ·
    <a href="https://github.com/mstatt/Emotion_Detection/issues">Report Bug</a>
    ·
    <a href="https://github.com/mstatt/Emotion_Detection/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Emotion Detector</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#toggles">Toggles</a></li>
    <li><a href="#output">Output</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Emotion Detection Application by Falcons.ai

In this project I wanted to test and deploy a web based emotion detection application. The application captures frames from the web cam and runs them against a pre-trained emotion detection model and then captures the output in either a sad, happy or an angry directory. During this prediction the output of all detected emotions are written to a camera-log.csv log file, that upon clicking the detection off wil render in a dataframe to the webpage.


Use this `README.md` to get started.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

This application was built using Anaconda Python, Streamlit and a pre-trained emotion detection model.

* [Anaconda Python](https://www.anaconda.com/products/individual)
* [Streamlit](https://docs.streamlit.io/library/get-started)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

In order to get this project up and running it is assumed that you have downloaded and installed Anaconda Python and updated all dependencies to their latest versions..

### Prerequisites

After installing Anaconda Python the command below will update the packages for you using the terminal or cmd prompt.
* Anaconda Python
  ```sh
  conda --update-all
  ```
  
 Create a new Python enviorment using the requirements.txt file.
* Create New Env
  ```sh
  conda create --name <env_name> --file requirements.txt
  ```


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

 Activate the enviornment.
* Once you created the enviornment, you need to activate it using the following command.
  ```sh
  conda activate <env_name>
  ```


 Launch the application.
* Using streamlit to launch the application locally. Navigate to the directory where the "main_app.py" is located and run the following command in the terminal.
  ```sh
  streamlit run main_app.py
  ```
 
 <!-- TOGGLES -->
## Toggles
 
  
   Toggles.
* You can also toggle on and off the image write functionality by editing the main_app.py file: Change switch = True.
  ```sh
  switch = False
  ```
* You can also toggle on and off the log write functionality by editing the main_app.py file: Change log_switch = True.
  ```sh
  log_switch = False
  ```
  
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- OUTPUT -->
## Output

In the images below you can see still shots of the application runnning on your local machine. When deployed to Streamlit platform there are obstacles to accessing the users web cam through the browser that I and others have yet to overcome. But, It does work fine locally.

Happy Detection            |  Angry Detection
:-------------------------:|:-------------------------:
![happy-screenshot] |  ![angry-screenshot]

Surprised Detection            |  Neutral Detection
:-------------------------:|:-------------------------:
![surprise-screenshot] |  ![neutral-screenshot]






<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you want feel free to fork the repo You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request
<br />
See the [open issues](https://github.com/mstatt/Emotion_Detection/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/mstatt/Emotion_Detection]

<p align="right">(<a href="#top">back to top</a>)</p>






<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/mstatt/Emotion_Detection/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mikestattlelman/
[happy-screenshot]: assets/happy.png
[angry-screenshot]: assets/angry.png
[neutral-screenshot]: assets/neutral.png
[surprise-screenshot]: assets/surprise.png

