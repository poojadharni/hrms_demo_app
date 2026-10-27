### HRMS Demo Portal

A lightweight HRMS portal for employee records and everyday people operations.

For local development, Admin, Employee and HR buttons on the login page can sign
in using credentials kept in `sites/<site>/site_config.json`:

```json
{
  "website_context": {
    "hrms_demo_users": {
      "admin": {
        "username": "admin@example.test",
        "password": "replace-with-a-local-demo-password"
      },
      "employee": {
        "username": "employee@example.test",
        "password": "replace-with-a-local-demo-password"
      },
      "hr": {
        "username": "hr@example.test",
        "password": "replace-with-a-local-demo-password"
      }
    }
  }
}
```

The quick-login endpoint is restricted to developer mode, local requests and
same-origin requests. It checks the supplied password against Frappe and
refuses accounts with two-factor authentication. Do not enable this on a
network-accessible or production site. Keep `site_config.json` private and out
of source control.
Use a dedicated Employee account; do not use `Administrator` for the Employee
role. Change any credentials shared in chat.
The HR account must have the Frappe `HR Manager` role and must not be an administrator.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch version-16
bench install-app hrms_demo_app
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/hrms_demo_app
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade
### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
