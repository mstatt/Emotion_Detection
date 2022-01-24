# Emotion_Detection

<div id="top"></div>
<div align="center">
  
![](https://img.shields.io/badge/Language-Python-blue)
![](https://img.shields.io/badge/Platform-Streamlit-red)
![](https://img.shields.io/badge/License-MIT-blue)
![](https://img.shields.io/github/issues/mstatt/Emotion_Detection)
  
</div>



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

In this project I wanted to test and deploy a web based emotion detection application. The application captures frames from the web cam and runs them against a pre-trained emotion detection model and then captures the output in either a sad, happy or an angry directory. During this prediction the output of all detected emotions are written to a camera-log.csv log file, that upon clicking the detection off will render in a dataframe to the webpage.


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
* You can also toggle on and off the image write functionality by editing the main_app.py file: Change switch = True. You may want to consider this if space is an issue as every Happy, Sad and Angry frame detection gets written to the drive.
  ```sh
  switch = False
  ```
* You can also toggle on and off the log write functionality by editing the main_app.py file: Change log_switch = True. Similar to the image write functionality, you may want to turn this off as the file can get really large based on the write per detection rate.
  ```sh
  log_switch = False
  ```
  
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- OUTPUT -->
## Output

In the images below you can see still shots of the application runnning on your local machine. When deployed to Streamlit platform there are obstacles to accessing the users web cam through the browser that I and others have yet to overcome. But, It does work fine on your local machine.

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

If you want, feel free to fork this repository. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request
<br />
See the https://github.com/mstatt/Emotion_Detection/issues for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

[![Licence][license-shield]][license-url]

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/mstatt/Emotion_Detection]

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: assets/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6f74686e65696c647265772f426573742d524541444d452d54656d706c6174652e7376673f7374796c653d666f722d7468652d6261646765.svg?style=for-the-badge
[license-url]: https://github.com/mstatt/Emotion_Detection/blob/main/LICENSE.txt
[demo-url]: https://www.youtube.com/watch?v=AWB2cEKcME0
[demo-shield]: https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white
[happy-screenshot]: assets/happy.png
[angry-screenshot]: assets/angry.png
[neutral-screenshot]: assets/neutral.png
[surprise-screenshot]: assets/surprise.png

