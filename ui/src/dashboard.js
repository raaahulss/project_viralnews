import React, { Component } from 'react'
import ArticleDetails from './components/article_details'
import Analysis from './components/analysis'
import Statistics from './components/statistics'

class Dashboard extends Component {
  constructor(props){
    super(props);
  }
  render() {
    let response = {
      "published": true,
      "models": {
        "viralness": 0.77,
        "sentiment": 0.23,
        "public_opinion": 0.88
      },
      "details": {
        "title": "abc",
        "source": "def",
        "authors": "ghi",
        "published_date": "1591080596",
    //    "last_updated": "1591080599",
        "content": "jkl",
        "op_url": "www.mno.com"
      },
      "metrics": {
        "retweets": 1234567,
        "favourites": 1234567,
        "responses": 1234567,
        "trending": "Yes",
        "first_tweet": "6:00 PM, June 05, 2020",
        "last_tweet": "8:45 PM, June 05, 2020"
      },
      "metadata": {
        "error": true,
        "error_code": "ERR_XYZ"
      }
    }
    if (response.published === true) {
      return (
        <div>
          <ArticleDetails />
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
