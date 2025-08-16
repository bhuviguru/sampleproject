import { InputFieldStylesProps, InputFieldStyles } from './InputField.types';

export const getInputFieldStyles = (props: InputFieldStylesProps): InputFieldStyles => {
  const { variant, size, disabled, invalid, focused } = props;
  
  const baseClasses = 'input-field';
  const variantClasses = `input-field--${variant}`;
  const sizeClasses = `input-field--${size}`;
  const stateClasses = [
    disabled && 'input-field--disabled',
    invalid && 'input-field--invalid',
    focused && 'input-field--focused'
  ].filter(Boolean).join(' ');
  
  return {
    label: `${baseClasses}__label`,
    inputWrapper: `${baseClasses}__wrapper ${variantClasses} ${sizeClasses} ${stateClasses}`,
    input: `${baseClasses}__input`,
    message: `${baseClasses}__message ${invalid ? 'input-field__message--error' : 'input-field__message--helper'}`
  };
}; 