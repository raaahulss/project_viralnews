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
        "viralness": 0.5,
        "sentiment": 0.5,
        "public_opinion": 0.5
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
        "retweets": 123,
        "favourites": 456,
        "responses": 789,
        "trending": "Yes",
        "first_tweet": "6:00 PM, June 05, 2020",
        "last_tweet": "8:45 PM, June 05, 2020"
      },
      "metadata": {
        "error": true,
        "error_code": "ERR_XYZ"
      }
    }
    return (
      <div>
        <ArticleDetails />
        <Analysis />
        <Statistics metrics={response.metrics}/>
      </div>
    );
  }
}

export default Dashboard;
