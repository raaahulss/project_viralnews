import React, { Component } from 'react'
import ArticleDetails from './components/article_details'
import Analysis from './components/analysis'
import Statistics from './components/statistics'
import ErrorCard from './components/error_card'


class Dashboard extends Component {
  constructor(props){
    super(props);
  }
  render() {
    //let response = this.props.location.state.data
    let response = this.props.location.state
    console.log(response);

    if (response.error !== "") {
      return (
        <ErrorCard error={response.error}/>
      )
    } else {
        if (response.input_type === "UnPub") {
          return (
            <div>
              <ArticleDetails title={response.details.title}
                              url={response.details.op_url}
                              source={response.details.source}
                              author={response.details.authors}
                              date={response.details.published_date}
                              content={response.details.content}/>
              <Analysis models={response.models} input_type={response.input_type}/>
            </div>
          );
        } else if (response.input_type === "Twitter") {
            return (
              <div>
                <ArticleDetails title={response.details.title}
                                url={response.details.op_url}
                                source={response.details.source}
                                author={response.details.authors}
                                date={response.details.published_date}
                                content={response.details.content}/>
                <Analysis models={response.models} input_type={response.input_type}/>
                <Statistics metrics={response.metrics}/>
              </div>
            );
        } else if (response.input_type === "NonTwitter") {
            return (
              <div>
                <ArticleDetails title={response.details.title}
                                url={response.details.op_url}
                                source={response.details.source}
                                author={response.details.authors}
                                date={response.details.published_date}
                                content={response.details.content}/>
                <Analysis models={response.models} input_type={response.input_type}/>
              </div>
          );
        }
    }
  }
}

export default Dashboard;
