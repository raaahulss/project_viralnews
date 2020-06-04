import React, { Component } from 'react'
import ArticleDetails from './components/article_details'
import Analysis from './components/analysis'
import Statistics from './components/statistics'

class Dashboard extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <div>
        <ArticleDetails />
        <Analysis />
        <Statistics />
      </div>
    );
  }
}

export default Dashboard;
