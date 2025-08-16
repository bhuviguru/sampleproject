import React from 'react';

export interface InputFieldProps {
  value?: string;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
  label?: string;
  placeholder?: string;
  helperText?: string;
  errorMessage?: string;
  disabled?: boolean;
  invalid?: boolean;
  variant?: 'filled' | 'outlined' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
}

export interface InputFieldStylesProps {
  variant: 'filled' | 'outlined' | 'ghost';
  size: 'sm' | 'md' | 'lg';
  disabled: boolean;
  invalid: boolean;
  focused: boolean;
}

export interface InputFieldStyles {
  label: string;
  inputWrapper: string;
  input: string;
  message: string;
} 