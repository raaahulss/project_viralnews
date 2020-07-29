import React, { Component } from 'react'
import GaugeChart from 'react-gauge-chart'

class SentimentMeter extends Component {
  render() {
    return (
      <div>
        <GaugeChart id="gauge-chart3"
          nrOfLevels={10}
          arcWidth={0.4}
          percent={this.props.value}
          textColor={'#e27d60'}
          colors={ ['#0000cc', '#0000e6' ,'#1a53ff', '#0066ff', '#0099ff',
                    '#ff704d', '#ff471a', '#ff471a' ,'#ff3300', '#ff0000']}
          style={{width: 300}}
          hideText={"True"}
        />
      </div>
    );
  }
}

export default SentimentMeter;
