import './App.css';
import './index.css';

import Main from './components/Main';
import Page from './components/Page';

function App() {
  return (
    <div className="App">
      <Page>
        <Main />
      </Page>
    </div>
  );
}

export default App;
