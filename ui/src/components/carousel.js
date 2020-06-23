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
            <h1>Viral: The top 50% of retweets based off of our dataset</h1>
              <p>  In the Viral News project, we look at viral news articles, focusing on articles about
                U.S. politics specifically. We observe the features that make an article prone to
                going viral. This product is focusing on two target groups: journalists and news
                consumers. However, we still aim to provide valuable research which helps us better
                understand what makes certain articles go viral in order to contribute to the fight
                against disinformation campaigns.</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block w-100"
            src={bias}
            alt="Third slide"
          />

          <Carousel.Caption>
            <h1>Politcal Bias: The magnitude and political direction implicit in an article </h1>
            <p>This service detects the underlying political sentiment in a U.S. political news
                      article. We have used various machine learning models to detect whether an
                      article is leaning more towards democratic or republican. Since our targeted audience
                      are journalists and general users, we think detecting the political bias with respect to
                      two major U.S. political parties can provide useful insights for our users. What’s more,
                      the underlying political bias of a U.S. news article may have a correlation with its
                      popularity and we plan to identify this potential correlation.</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block w-100"
            src={sentiment}
            alt="Third slide"
          />

          <Carousel.Caption>
          <h1>Public Sentiment: Positive and negative as defined by our dataset </h1>
          <p> As a part of Viral News project, this service analyzes how the general public
                      (twitter users) reacts to news articles on U.S. politics. We provide concrete statistics
                      including percentage of positive opinions and percentage of negative opinions. We
                      have used various machine learning models to predict a user’s opinion on the
                      article. These models are specifically trained on the language used in Twitte.</p>
          </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
      </div>
    );
  }
}

export default CarouselMl
