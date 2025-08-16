import { useState, forwardRef } from 'react';
import { InputFieldProps } from './InputField.types';
import { getInputFieldStyles } from './InputField.styles';

export const InputField = forwardRef<HTMLInputElement, InputFieldProps>(
  (
    {
      value = '',
      onChange,
      label,
      placeholder,
      helperText,
      errorMessage,
      disabled = false,
      invalid = false,
      variant = 'outlined',
      size = 'md'
    },
    ref
  ) => {
    const [isFocused, setIsFocused] = useState(false);

    const hasError = invalid || !!errorMessage;

    const styles = getInputFieldStyles({
      variant,
      size,
      disabled,
      invalid: hasError,
      focused: isFocused
    });

    return (
      <div className="input-field-container">
        {label && (
          <label className={styles.label}>
            {label}
          </label>
        )}
        
        <div className={styles.inputWrapper}>
          <input
            ref={ref}
            type="text"
            value={value}
            onChange={onChange}
            placeholder={placeholder}
            disabled={disabled}
            className={styles.input}
            onFocus={() => setIsFocused(true)}
            onBlur={() => setIsFocused(false)}
          />
        </div>
        
        {(helperText || errorMessage) && (
          <div className={styles.message}>
            {errorMessage || helperText}
          </div>
        )}
      </div>
    );
  }
);

InputField.displayName = 'InputField'; 