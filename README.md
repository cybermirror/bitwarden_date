# bitwarden_date
To convert serial date number to yyyy-mm-dd in bitwarden json file

When import 1pif (1Password file) to bitwarden, the date fields in 1Password are converted to serial date numbers in bitwarden.
User can hardly read the serial date number in bitwarden. This python code read the json file exported from bitwarden vault and convert the serial date number to yyyy-mm-dd. The output is the same json file with date format converted.
