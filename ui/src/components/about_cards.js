import React, {Component} from 'react'
import {Card, CardDeck} from 'react-bootstrap';
import '../css/about.css'
import fz from './img/fz.png';
import rs from './img/i.jpeg';
import gd from './img/gd.jpeg';
import st from './img/teplov.jpeg';
import am from './img/aomellinger.jpg'
import jm from './img/moritz-jen.jpg'
import stel from './img/st.jpeg';

class AboutCards extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <div className = "jumbo_pad">
          <h2 className="api_title">About our Project</h2>
          <div id="body_par">
            <p>
              The goal of our project is to enable the analysis of viral news in order to better understand how disinformation is spread. Our platform will provide journalists, analysts, and researchers with a number of tools for analyzing viral news during the 2020 U.S. presidential election news cycle.
            </p>
          </div>

        <div className = "about_section">
        <h2 className="api_title">Developer Team</h2>
        <CardDeck>
          <Card border="primary" style={{ width: '18rem' }}>
            <Card.Img variant="top" src={fz} />
            <Card.Body>
              <Card.Title>Fangzhou Xie</Card.Title>
              <Card.Text>
                Backend Developer, ML Researcher
              </Card.Text>
            </Card.Body>
            <Card.Footer>
              <Card.Link href="#">GitHub</Card.Link>
              <Card.Link href="#">Linkedin</Card.Link>
            </Card.Footer>
          </Card>
          <Card border="primary"style={{ width: '5rem' }}>
            <Card.Img variant="top" src={rs} />
            <Card.Body>
              <Card.Title>Rahul Salla</Card.Title>
              <Card.Text>
                Frontend Developer, ML Researcher
              </Card.Text>
            </Card.Body>
            <Card.Footer>
              <Card.Link href="#">GitHub</Card.Link>
              <Card.Link href="#">Linkedin</Card.Link>
            </Card.Footer>
          </Card>
          <Card border="primary"style={{ width: '5rem' }}>
            <Card.Img variant="top" src={gd} />
            <Card.Body>
              <Card.Title>Gaurav Deshpande</Card.Title>
              <Card.Text>
                Backend Developer, ML Researcher
              </Card.Text>
            </Card.Body>
            <Card.Footer>
              <Card.Link href="#">GitHub</Card.Link>
              <Card.Link href="#">Linkedin</Card.Link>
            </Card.Footer>
          </Card>
          <Card border="primary"style={{ width: '5rem' }}>
            <Card.Img variant="top" src={st} />
            <Card.Body>
              <Card.Title>Sam Teplov</Card.Title>
              <Card.Text>
                Frontend Developer, ML Researcher
              </Card.Text>
            </Card.Body>
            <Card.Footer>
              <Card.Link href="#">GitHub</Card.Link>
              <Card.Link href="#">Linkedin</Card.Link>
            </Card.Footer>
          </Card>
        </CardDeck>
        </div>

        <div className="about_section">
          <h2 className="api_title">CMU Faculty Team</h2>


          <CardDeck>
            <Card border="primary">
              <Card.Img variant="top" src={am} />
              <Card.Body>
                <Card.Title>Andrew Mellinger</Card.Title>
                <Card.Text>
                  Team Mentor, SEI
                </Card.Text>
              </Card.Body>
              <Card.Footer>
                <Card.Link href="#">GitHub</Card.Link>
                <Card.Link href="#">Linkedin</Card.Link>
              </Card.Footer>
            </Card>
            <Card border="primary">
              <Card.Img variant="top" src={jm} />
              <Card.Body>
                <Card.Title>Jennifer Moritz</Card.Title>
                <Card.Text>
                  Customer, CMU ISR
                </Card.Text>
              </Card.Body>
              <Card.Footer>
                <Card.Link href="#">GitHub</Card.Link>
                <Card.Link href="#">Linkedin</Card.Link>
              </Card.Footer>
            </Card>
            <Card border="primary">
              <Card.Img variant="top" src={stel} />
              <Card.Body>
                <Card.Title>Sujata Telang</Card.Title>
                <Card.Text>
                  Technical Advisor, CMU ISR
                </Card.Text>
              </Card.Body>
              <Card.Footer>
                <Card.Link href="#">GitHub</Card.Link>
                <Card.Link href="#">Linkedin</Card.Link>
              </Card.Footer>
            </Card>
          </CardDeck>
          </div>

    </div>
    );
  }
}

export default AboutCards
