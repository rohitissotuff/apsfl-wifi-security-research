
# Research Notes: APSFL Wi-Fi Password Patterns

## 1. Background

This project investigates a password format observed in connection with legacy APSFL Wi-Fi equipment.

The pattern under investigation consists of a fixed six-zero prefix (`000000`) followed by a four-character alphanumeric suffix.

This is an observed pattern and research hypothesis, not a verified rule for every APSFL router.

## 2. Research Objective

The objective is to understand how predictable password-generation formats affect wireless security.

The research focuses on:

- Examining the structure of a suspected password format.
- Understanding the theoretical search space.
- Evaluating the limitations of predictable password schemes.
- Promoting unique and randomly generated Wi-Fi credentials.

## 3. Password-Space Mathematics

The number of possible suffixes depends on the character set and suffix length.

For a four-character suffix:

| Character set | Calculation | Combinations |
|---|---|---:|
| Lowercase letters and digits | 36^4 | 1,679,616 |
| Uppercase and lowercase letters and digits | 62^4 | 14,776,336 |

These calculations assume that every character in the selected set is allowed in every position and that repetitions are permitted.

The Python implementation uses `string.ascii_letters` and `string.digits`, so uppercase and lowercase letters are treated as distinct.

## 4. Generator Methodology

The project uses Python's standard library, including `itertools` and `string`, to demonstrate combinatorial generation.

The generator illustrates how a fixed prefix and a defined character set can produce a finite set of possible strings.

The generated candidates are theoretical possibilities. Their existence does not establish that any candidate is an actual password used by a particular network.

## 5. Security Implications

A predictable password format can reduce uncertainty when compared with independently generated, random credentials.

The security of a password depends on the actual generation process, the permitted character set, the length, and whether the pattern is known or predictable.

A large number of possible combinations does not, by itself, establish that a password scheme is secure.

## 6. Testing Applications

Password-pattern research can support defensive security assessments in isolated laboratories and on systems for which explicit authorisation has been obtained.

Useful areas of study include:

- Comparing theoretical and observed password distributions.
- Analysing character sets and search-space sizes.
- Measuring the uniqueness of generated credentials.
- Evaluating password policies and default-credential practices.

## 7. Limitations

- The observed pattern may not apply to every APSFL device or installation.
- The pattern has not been established as a universal vendor rule.
- Generated candidates are not verified passwords.
- Theoretical calculations do not establish the security of a specific network.
- The findings should not be generalised beyond the available evidence.

## 8. Responsible Use

This research is intended for educational and defensive purposes.

Testing must be limited to equipment and networks owned by the researcher or covered by explicit authorisation. Unauthorised access and disruption of network services are outside the intended scope.

## 9. Conclusion

Predictable password formats can introduce security weaknesses, even when the resulting search space appears large.

This project uses combinatorial analysis to explore that risk and highlight the importance of unique credentials, secure provisioning, and responsible security testing.
