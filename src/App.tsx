import React, { useState } from 'react';
import { InputField } from './components/InputField';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    basic: '',
    email: '',
    disabled: 'Disabled input',
    invalid: 'Invalid input'
  });

  const handleInputChange = (field: string) => (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData(prev => ({
      ...prev,
      [field]: e.target.value
    }));
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>InputField Component Demo</h1>
        <p>A flexible input component with validation states, variants, and sizes</p>
      </header>

      <main className="app-main">
        <section className="demo-section">
          <h2>Basic Input Fields</h2>
          <div className="demo-grid">
            <InputField
              label="Basic Input"
              placeholder="Enter some text..."
              value={formData.basic}
              onChange={handleInputChange('basic')}
            />
            
            <InputField
              label="Required Field"
              placeholder="This field is required"
              helperText="This field must be filled out"
            />
            
            <InputField
              label="With Helper Text"
              placeholder="Enter your email"
              helperText="We'll never share your email with anyone else"
              value={formData.email}
              onChange={handleInputChange('email')}
            />
          </div>
        </section>

        <section className="demo-section">
          <h2>Input Variants</h2>
          <div className="demo-grid">
            <InputField
              label="Outlined Variant (Default)"
              placeholder="Outlined style"
              variant="outlined"
            />
            
            <InputField
              label="Filled Variant"
              placeholder="Filled style"
              variant="filled"
            />
            
            <InputField
              label="Ghost Variant"
              placeholder="Ghost style"
              variant="ghost"
            />
          </div>
        </section>



        <section className="demo-section">
          <h2>Input Sizes</h2>
          <div className="demo-grid">
            <InputField
              label="Small Size"
              placeholder="Small input"
              size="sm"
            />
            
            <InputField
              label="Medium Size (Default)"
              placeholder="Medium input"
              size="md"
            />
            
            <InputField
              label="Large Size"
              placeholder="Large input"
              size="lg"
            />
          </div>
        </section>

        <section className="demo-section">
          <h2>Input States</h2>
          <div className="demo-grid">
            <InputField
              label="Disabled Input"
              value={formData.disabled}
              disabled
              helperText="This input is disabled"
            />
            
            <InputField
              label="Invalid Input"
              value={formData.invalid}
              invalid
              errorMessage="This field has an error"
            />
            

          </div>
        </section>

        <section className="demo-section">
          <h2>Complex Examples</h2>
          <div className="demo-grid">
            <InputField
              label="Email with Validation"
              placeholder="Enter your email address"
              helperText="Please enter a valid email address"
              variant="filled"
              size="lg"
            />
            
            <InputField
              label="Required Field"
              placeholder="This field is required"
              variant="outlined"
              size="md"
              helperText="This field must be filled out"
            />
            
            <InputField
              label="Ghost Variant Small"
              placeholder="Small ghost input"
              variant="ghost"
              size="sm"
              helperText="This is a small ghost variant"
            />
          </div>
        </section>
      </main>
    </div>
  );
}

export default App; 