import React, { Component } from 'react'

class ArticleEntry extends Component {
  constructor(props){
    super(props);
  }
  render() {
    if (this.props.value !== "") {
      return(
        <div>
          {this.props.field}: {this.props.value}
          <br />
        </div>
      )
    } else {
      return(null);
    }
  }
}

export default ArticleEntry;
