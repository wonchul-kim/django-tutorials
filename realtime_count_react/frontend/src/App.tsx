import React from "react";
import "./App.css";

interface IState {
  info: string;
  data: number;
}

class App extends React.Component<{}, IState> {
  ws: any;

  state = {
    info: "",
    data: 0,
  }

  componentDidMount() {
    this.ws = new WebSocket("ws://localhost:8000/ws/integers/");
    this.ws.onopen = () => {
      this.ws.send(JSON.stringify({
        "message": "Hello! from Client",
      }))
    };

    this.ws.onmessage = (e: MessageEvent) => {
      var data = JSON.parse(e.data);
      console.log(data);
      if (data.type == "INFO")
        this.setState({
          info: data.message
        })
      else if (data.type == "TRAIN")
        this.setState({
          data: data.message
        })
    };
  }

  startButton = () => {
    console.log("startButton")
    this.ws.send(JSON.stringify({
      "message": "start"
    }))
  };
  stopButton = () => {
    console.log("stopButton")
    this.ws.send(JSON.stringify({
      "message": "stop"
    }))
  };
  render() {
    return (
      <div className="App">
        <h1>
        {this.state.data}
        </h1>
        <header className="App-header">
          <button onClick={this.startButton}>start</button>
          <button onClick={this.stopButton}>stop</button>
        </header>
      </div>
    );
  }
}

export default App;