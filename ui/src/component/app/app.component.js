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
        <div className="jumbotron mb3">
            <h1 className="display-4 text-center">Project Viral News</h1>
            <hr class="my-4"></hr>
            <button type="button" className="btn btn-primary btn-lg " onClick={props.onClick}>Return</button>
            <p>{props.text}</p>
        </div>
    );
}
function WithURL(props) {
    return (
        <div className="jumbotron mb3">
            <h1 className="display-4 text-center">Project Viral News</h1>
            <hr class="my-4"></hr>
            <form>
            <div class="form-group">
                <div class="input-group input-group-lg">
                    <div class="input-group-prepend">
                        <span class="input-group-text" id="inputGroup-sizing-lg">URL</span>
                    </div>
                    <input type="text" class="form-control" name="url" aria-label="URL" aria-describedby="inputGroup-sizing-sm" onChange={props.onUrlChange}  value={props.value}></input>
                    {/* <input type="text" class="form-control" name="url" aria-label="URL" aria-describedby="inputGroup-sizing-sm" /> */}
                </div>
            </div>
            <div className="row">
            <div class="col-sm"></div>
            <div class="col-sm">
                <button className="btn btn-primary btn-lg btn-block" type="button" onClick={props.onClick}>
                Submit
            </button>
            </div>
            <div class="col-sm"></div> 
            </div>
                {/* <label>Url link</label>
                <input type="text" name="url" onChange={props.onUrlChange}  value={props.value}></input>*/}
                
            </form>
        </div>
    );
}
export default App;