import React, { Component } from 'react'
import ArticleDetails from './components/article_details'
import Analysis from './components/analysis'
import Statistics from './components/statistics'


class Dashboard extends Component {
  constructor(props){
    super(props);
  }
  render() {
    /*
    let response = {
      "published": true,
      "models": {
        "viralness": 0.77,
        "sentiment": 0.23,
        "public_opinion": 0.88
      },
      "details": {
        "title": "Two more Trump staffers test positive for coronavirus after Tulsa rally",
        "source": "CNN",
        "authors": "Maegan Vazquez",
        "published_date": "3:30 PM ET, Fri June 5, 2020",
    //    "last_updated": "1591080599",
        "content": "President Donald Trump invoked George Floyd's name during a Friday bill signing ceremony touting the latest jobs report, which exceeded economists' expectations.",
        "op_url": "https://www.cnn.com/2020/06/05/politics/donald-trump-george-floyd-rose-garden/index.html"
      },
      "metrics": {
        "retweets": 432,
        "favourites": 874,
        "responses": 45,
        "trending": "Yes",
        "first_tweet": "6:00 PM, June 05, 2020",
        "last_tweet": "8:45 PM, June 05, 2020"
      },
      "metadata": {
        "error": true,
        "error_code": "ERR_XYZ"
      }
    }*/
    //let response = this.props.location.state.data
    let response = this.props.location.state
    if (response.published === true) {
      return (
        <div id="margin-top: 30px">
        <ArticleDetails title={response.details.title}
                        url={response.details.op_url}
                        source={response.details.source}
                        author={response.details.authors}
                        date={response.details.published_date}
                        content={response.details.content}/>
          <Analysis models={response.models} published={response.published}/>
          <Statistics metrics={response.metrics}/>

        </div>
      );
    } else {
      return (
        <div>
          <ArticleDetails />
          <Analysis models={response.models} published={response.published}/>
        </div>
      );
    }

  }
}

export default Dashboard;
