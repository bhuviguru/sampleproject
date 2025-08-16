# InputField Component

A flexible and feature-rich React input component with comprehensive validation states, multiple variants, sizes, and accessibility features.

## 🚀 Features

### Core Features
- **Text input** with label, placeholder, helper text, and error message support
- **Multiple states**: disabled, invalid
- **Three variants**: filled, outlined, ghost
- **Three sizes**: small (sm), medium (md), large (lg)
- **Theme support**: Light & dark theme with CSS custom properties

### Accessibility Features
- Proper ARIA labels and descriptions
- Keyboard navigation support
- Focus management with visible focus indicators
- High contrast mode support
- Screen reader friendly

### Responsive Design
- Mobile-first approach
- Adaptive sizing for different screen sizes
- Touch-friendly interactive elements

## 📦 Installation

```bash
npm install
```

## 🏃‍♂️ Development

```bash
npm run dev
```

This will start the development server at `http://localhost:3000`

## 🏗️ Build

```bash
npm run build
```

## 📖 Usage

### Basic Usage

```tsx
import { InputField } from './components/InputField';

function MyForm() {
  const [value, setValue] = useState('');

  return (
    <InputField
      label="Email Address"
      placeholder="Enter your email"
      value={value}
      onChange={(e) => setValue(e.target.value)}
      helperText="We'll never share your email"
    />
  );
}
```

### With Validation

```tsx
<InputField
  label="Password"
  type="password"
  placeholder="Enter your password"
  passwordToggle
  invalid={!isValidPassword}
  errorMessage="Password must be at least 8 characters"
  required
/>
```

### Different Variants and Sizes

```tsx
{/* Outlined variant, medium size (default) */}
<InputField
  label="Standard Input"
  variant="outlined"
  size="md"
/>

{/* Filled variant, large size */}
<InputField
  label="Large Filled Input"
  variant="filled"
  size="lg"
/>

{/* Ghost variant, small size */}
<InputField
  label="Small Ghost Input"
  variant="ghost"
  size="sm"
/>
```

### With Special Features

```tsx
<InputField
  label="Search Products"
  type="search"
  placeholder="Search for products..."
  clearable
  loading={isSearching}
  helperText="Type to search products"
/>
```

## 🔧 Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` | `string` | `''` | The current value of the input |
| `onChange` | `(e: React.ChangeEvent<HTMLInputElement>) => void` | - | Callback fired when the input value changes |
| `label` | `string` | - | Label text displayed above the input |
| `placeholder` | `string` | - | Placeholder text displayed when input is empty |
| `helperText` | `string` | - | Helper text displayed below the input |
| `errorMessage` | `string` | - | Error message displayed below the input (overrides helperText) |
| `disabled` | `boolean` | `false` | Whether the input is disabled |
| `invalid` | `boolean` | `false` | Whether the input is in an invalid state |
| `variant` | `'filled' \| 'outlined' \| 'ghost'` | `'outlined'` | Visual variant of the input |
| `size` | `'sm' \| 'md' \| 'lg'` | `'md'` | Size of the input |
| `type` | `string` | `'text'` | HTML input type |
| `clearable` | `boolean` | `false` | Whether to show a clear button when input has value |
| `passwordToggle` | `boolean` | `false` | Whether to show password toggle for password inputs |
| `loading` | `boolean` | `false` | Whether to show loading state |
| `className` | `string` | `''` | Additional CSS class name |
| `required` | `boolean` | `false` | Whether the field is required |

## 🎨 Styling

The component uses CSS custom properties for theming and supports both light and dark themes automatically. You can customize the appearance by overriding CSS variables:

```css
:root {
  --input-label-color: #374151;
  --input-border-color: #d1d5db;
  --input-focus-color: #3b82f6;
  --input-error-color: #dc2626;
  --input-helper-color: #6b7280;
}
```

### CSS Classes

The component generates BEM-style CSS classes:
- `.input-field-container` - Main container
- `.input-field__label` - Label element
- `.input-field__wrapper` - Input wrapper with variants and states
- `.input-field__input` - Actual input element
- `.input-field__actions` - Container for action buttons
- `.input-field__message` - Helper text or error message

## 🌙 Dark Theme

The component automatically detects and adapts to the user's preferred color scheme using `@media (prefers-color-scheme: dark)`. All colors are defined using CSS custom properties for easy customization.

## 📱 Responsive Design

The component is fully responsive and includes:
- Mobile-first CSS approach
- Adaptive sizing for different screen sizes
- Touch-friendly interactive elements
- Responsive grid layout in the demo

## ♿ Accessibility

- **ARIA Labels**: Proper labeling for screen readers
- **Focus Management**: Visible focus indicators and keyboard navigation
- **High Contrast**: Support for high contrast mode
- **Semantic HTML**: Proper use of HTML elements and attributes
- **Keyboard Support**: Full keyboard navigation support

## 🔍 Browser Support

- Modern browsers with ES2020 support
- CSS Grid and Flexbox support required
- CSS custom properties support required

## 📁 Project Structure

```
src/
├── components/
│   └── InputField/
│       ├── InputField.tsx          # Main component
│       ├── InputField.types.ts     # TypeScript types
│       ├── InputField.styles.ts    # Style utilities
│       ├── InputField.icons.tsx    # SVG icons
│       ├── InputField.css          # Component styles
│       └── index.ts                # Exports
├── App.tsx                         # Demo application
├── App.css                         # Demo styles
└── main.tsx                        # Entry point
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🎯 Roadmap

- [ ] Add more input types (textarea, select, etc.)
- [ ] Add form validation integration
- [ ] Add more variants and themes
- [ ] Add animation support
- [ ] Add unit tests
- [ ] Add Storybook documentation 