### HR Empoyee Custom App

Custom app for Employee and HR

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app hr_custom
bench --site [site_name] migrate
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/hr_custom
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit

### Features

1. Workflow setup for Hiring Employee
2. Workflow setup for Employee Lifecycle
3. Report for Applicant's Source
4. Custom Experience Letter for Employee exiting
5. Custom Salary Slip
6. Setup for Old and New Tax Regime in Salary Structure
7. Comparision Report for Old vs New Regime
8. Employee Investment are now part of Payroll