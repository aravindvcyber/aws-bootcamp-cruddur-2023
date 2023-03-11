import { render, screen } from '@testing-library/react';
import App from './App';

test('renders crudder frontend app', () => {
  render(<App />);
  const linkElement = screen.getByText(/Join The Party!/i);
  expect(linkElement).toBeInTheDocument();
});
