import React, {Component} from 'react'
import * as Constants from '../constants'
class App extends Component{
    constructor(){
        super();
        this.state = {url:"",
                isClicked:false,
                text : "" };
        // this.getData = this.getData.bind(this);
    }
    onUrlChange = (e) =>{
        this.setState({url:e.target.value});
    }

    getData = () => {
        // this.state.url =!this.state.url;
        console.log(Constants.parse, this.state.url, this.state.isClicked);
        const options = {
            method : 'GET',
        };
        fetch(Constants.parse+"?url="+this.state.url, options)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                this.setState({
                    isClicked : !this.state.isClicked,
                    text : data.response
                });
            }).catch(error =>{
                console.log(error);
            });
        
        
    }
    render(){
        let info;
        if(!this.state.isClicked){
            info = <WithURL onClick={this.getData} value={this.state.url} onUrlChange={this.onUrlChange}/>
        }else{
            info = <WithoutURL onClick={this.getData} text={this.state.text} />
        }
        return(
            <div>
                {info}
            </div>
        );
    }
}

function WithoutURL(props) {
    return (
        <div>
            <h1>Project Idk</h1>
            <button type="button" onClick={props.onClick}>Return</button>
            <p>{props.text}</p>
        </div>
    );
}
function WithURL(props) {
    return (
        <div>
            <h1>Project Idk</h1>
            <form>
                <label>Url link</label>
                <input type="text" name="url" onChange={props.onUrlChange}  value={props.value}></input>
                <button type="button" onClick={props.onClick}>Submit</button>
            </form>
        </div>
    );
}
export default App;