import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="premium-container">
      <nav style={{ padding: '2rem 0', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h3 className="gradient-text" style={{ fontSize: '1.5rem' }}>MaxTest</h3>
        <div style={{ display: 'flex', gap: '2rem' }}>
          <a href="#" style={{ color: '#888', textDecoration: 'none' }}>Features</a>
          <a href="#" style={{ color: '#888', textDecoration: 'none' }}>Showcase</a>
          <a href="#" style={{ color: '#888', textDecoration: 'none' }}>Docs</a>
        </div>
      </nav>

      <main>
        <section className="hero-section">
          <div className="glow-orb" style={{ top: '10%', left: '20%' }}></div>
          <div className="glow-orb" style={{ bottom: '20%', right: '10%', animationDelay: '-4s' }}></div>
          
          <h1 style={{ fontSize: '5rem', marginBottom: '1.5rem' }}>
            Elevate Your <span className="gradient-text">Experience</span>
          </h1>
          <p style={{ fontSize: '1.25rem', color: '#888', maxWidth: '600px', margin: '0 auto 3rem' }}>
            A premium starting point for your next big idea. Built with Vite, React, and a passion for exceptional design.
          </p>
          
          <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center' }}>
            <button className="btn-primary" onClick={() => setCount(count + 1)}>
              Get Started <span style={{ opacity: 0.7 }}>({count})</span>
            </button>
            <a href="https://vite.dev" target="_blank" className="glass-card" style={{ padding: '0.75rem 1.5rem', borderRadius: '12px', textDecoration: 'none', color: 'white', display: 'flex', alignItems: 'center' }}>
              Read Docs
            </a>
          </div>
        </section>

        <section style={{ padding: '4rem 0', display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '2rem' }}>
          <div className="glass-card">
            <h3 style={{ marginBottom: '1rem' }}>Lightning Fast</h3>
            <p style={{ color: '#888' }}>Powered by Vite for near-instant HMR and optimized production builds.</p>
          </div>
          <div className="glass-card">
            <h3 style={{ marginBottom: '1rem' }}>Modern Stack</h3>
            <p style={{ color: '#888' }}>React 18+ with the latest features and a clean, modular architecture.</p>
          </div>
          <div className="glass-card">
            <h3 style={{ marginBottom: '1rem' }}>Premium Design</h3>
            <p style={{ color: '#888' }}>Tailored aesthetics with glassmorphism, gradients, and smooth animations.</p>
          </div>
        </section>
      </main>

      <footer style={{ marginTop: 'auto', padding: '4rem 0 2rem', borderTop: '1px solid var(--border-color)', textAlign: 'center', color: '#555' }}>
        <p>&copy; 2026 MaxTest. All rights reserved.</p>
      </footer>
    </div>
  )
}

export default App
