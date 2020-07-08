import React, {Component} from 'react'
import {Carousel} from 'react-bootstrap';
import viral from './img/test_image_1.jpeg';
import bias from './img/test_image_2.jpeg';
import sentiment from './img/test_image_3.jpg';
import '../css/carousel.css'

class CarouselMl extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
    <div className="slide">
      <Carousel>
        <Carousel.Item>
          <img
            className="d-block w-100"
            src={viral}
            alt="First slide"
          />
          <Carousel.Caption>
          <h1 id="h2-title">Article Viralness</h1>


              <p>  Using the median number of retweets in our dataset as the threshold
              between popular and unpopular articles allows us to set up a binary
              classification problem. We use a combination of metadata features
              (date published, time published, length of content, etc) and textual
              features (content, title) to train a neural network that can predict
              with 60% accuracy if a certain article will go viral. The purpose of
              this model is to provide insight into what features of an article cause
              it to go viral. The dataset used to train our model, as well as the retweet count
              thresholds for various sources can be found in our GitHub Repo.   </p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block w-100"
            src={bias}
            alt="Second slide"
          />

          <Carousel.Caption>
            <h1 id="h2-title-bias">Political Bias</h1>

            <p>This model detects the underlying political sentiment in a news
                      article. This is done by training the model on data from the Ideological Book Corpus (IBC) dataset, which
                      can be found in our Github Repo. Each sentence in the training dataset was hand-labeled using mechanical turk.
                      This model can be used to analyze either a published or unpublished article. This differs from the other two models since
                      this model only considers textual features as input (title and content).</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block w-100"
            src={sentiment}
            alt="Third slide"
          />

          <Carousel.Caption>
          <h1 id="h2-title-reac">Public Reaction</h1>
          <p> This model analyzes how the public is reacting to a published news article.
              First, we query Twitter using Twitter's premium API to get a sample of tweets that people
              have posted as responses to the news article. These responses are then fed into our neural
              network and then the model outputs whether the general public agrees or disagrees with the article.
              The dataset that was used to train our model can be found in our Github Repo.
        </p>
          </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
      </div>
    );
  }
}

export default CarouselMl
