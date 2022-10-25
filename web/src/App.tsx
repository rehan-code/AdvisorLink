import './App.css';
import Page from './components/Page';
import './index.css'

function App() {
  return (
    <>
    <Page>
      {/* HERO SECTION */}
      <div className='hero-section'>
        <div className='p-12 bg-blue-800 text-white'>
          <h1 className='text-6xl font-bold'>Welcome to AdvisorLink</h1>
          <h3 className='text-4xl italic'>Helping plan your education!</h3>
        </div>
      </div>
    </Page>
    </>
  );
}

export default App;
