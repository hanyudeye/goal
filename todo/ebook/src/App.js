import logo from './logo.svg';
// import './App.css';
import GaussianBlur from './components/GaussianBlur/index'

function f(){
  console.log("helo")
}

function App() {
  return (
    <div className="App">
      <GaussianBlur children={[1,2,4]}></GaussianBlur>
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <p>
          Edit <code>src/App.js</code> and save to reload.
          nice
          good
        </p>
        <a
          href='http://aming.xyz'
        >
          网站
        </a>
        <br />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          学习Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
