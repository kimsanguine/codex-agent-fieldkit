# 운영자용 시작 가이드

이 문서는 개발자가 아닌 운영자, 서비스 기획자, 보험 도메인 실무자가
`Codex Agent Fieldkit`을 처음 열었을 때 따라 하는 15-30분 실습 경로입니다.

목표는 멋진 챗봇을 만드는 것이 아니라, 안전한 공개 예시로 다음 루프를 직접
확인하는 것입니다.

```text
폴더 열기 -> Codex에게 점검 요청 -> 데모 실행 -> CSV 한 줄 수정
-> 평가 통과/실패 확인 -> 검증 기록과 인수인계 문서 업데이트
```

모든 예시는 `ACME Life`라는 가상의 보험사와 합성 데이터만 사용합니다. 실제
고객명, 계약번호, 청구서류, 내부 링크, 화면 캡처, API 키는 넣지 마세요.

## 먼저 알아둘 말

| 용어 | 쉬운 뜻 |
|---|---|
| 폴더 | 관련 파일을 한곳에 모아 둔 컴퓨터 안의 상자입니다. |
| repo root | 이 프로젝트의 가장 바깥 폴더입니다. 여기서는 `README.md`, `START_HERE.md`, `Makefile`이 보이는 위치입니다. |
| 터미널 | 명령어를 입력해 프로그램을 실행하는 창입니다. Codex나 Mac의 Terminal 앱에서 열 수 있습니다. |
| `make` | 긴 명령어를 짧게 실행하게 해 주는 버튼 이름 같은 도구입니다. 예: `make demo`는 데모 실행 버튼입니다. |
| CSV | 엑셀 표처럼 행과 열이 있는 텍스트 파일입니다. 이 예시에서는 FAQ 질문과 답변을 담습니다. |
| eval | 답변이 정답 기준을 만족하는지 자동으로 채점하는 평가입니다. |
| validation log | 어떤 명령을 실행했고, 결과가 어땠고, 남은 위험이 무엇인지 남기는 검증 기록입니다. |
| handoff | 다음 담당자가 이어받을 수 있도록 현재 상태, 검증 결과, 한계를 정리한 인수인계 문서입니다. |

## 15-30분 실습 경로

### 1. 올바른 폴더 열기

터미널에서 프로젝트의 가장 바깥 폴더로 이동합니다.

```bash
cd codex-agent-fieldkit
```

확인 명령:

```bash
pwd
ls
```

`ls` 결과에 아래 파일들이 보이면 올바른 위치입니다.

```text
README.md
START_HERE.md
Makefile
starter-kits
```

### 2. Codex에게 먼저 점검을 시키기

바로 수정하지 말고, Codex에게 프로젝트 구조를 먼저 설명하게 합니다.

```text
README.md, AGENTS.md, START_HERE.md,
starter-kits/faq-agent-lite/README.md를 읽어 주세요.

개발자가 아닌 보험 서비스 운영자에게 설명하듯이
이 프로젝트의 폴더 구조, 데모 실행 방법, 평가 방법,
validation_log.md와 handoff.md의 역할을 설명해 주세요.

아직 파일은 수정하지 마세요.
```

이 단계의 목표는 "내가 지금 어느 폴더에서 무엇을 만지는지"를 확인하는 것입니다.

### 3. 데모 실행하기

repo root에서 아래 명령을 실행합니다.

```bash
make demo
```

기대 결과:

- 합성 FAQ 질문이 실행됩니다.
- 답변에는 `FAQ-001` 같은 출처가 붙습니다.
- 실제 고객 정보나 내부 시스템 정보는 나오지 않습니다.

전체 검증을 한 번에 보려면 아래 명령을 실행합니다.

```bash
make validate
```

처음에는 통과하는 상태가 정상입니다.

### 4. CSV 한 줄 바꿔 보기

아래 파일을 엽니다.

```text
starter-kits/faq-agent-lite/data/sample_faqs.csv
```

예를 들어 `FAQ-001` 행의 답변에 공개 안전한 문장을 하나 추가합니다.

예시:

```text
This is a synthetic ACME Life example for operator training.
```

주의:

- 실제 보험 약관 문구를 붙여 넣지 마세요.
- 실제 고객 질문, 상담 이력, 청구 서류명을 넣지 마세요.
- 기존 답변에 있는 `billing-date change`, `per month`, `next invoice` 같은 핵심 표현을 지우면 eval이 실패할 수 있습니다.

### 5. eval 실패 또는 통과 확인하기

수정 후 평가를 실행합니다.

```bash
make eval
```

통과하면:

```text
eval score: 100.00% (20/20)
```

실패를 일부러 연습해 보고 싶다면, `FAQ-001` 답변에서 `billing-date change`
같은 핵심 표현을 잠깐 지운 뒤 `make eval`을 실행합니다. 그러면 golden set이
기대한 문구를 찾지 못해 실패할 수 있습니다.

실패를 확인했으면 바로 원래 뜻이 유지되도록 복구하고 다시 실행합니다.

```bash
make eval
make validate
```

운영자 관점에서 중요한 것은 실패 자체가 아니라, 실패를 보고 수정한 뒤 다시
검증했다는 기록입니다.

### 6. 검증 기록 업데이트하기

아래 파일에 오늘 실행한 명령과 결과를 한 줄 추가합니다.

```text
starter-kits/faq-agent-lite/docs/validation_log.md
```

기록 예시:

```markdown
| 2026-06-22 | `make eval` | Passed | Golden-set score 100% (20/20) after one synthetic FAQ wording update | `FAQ-001` kept required public-safe terms |
```

만약 실패를 확인했다면 실패도 숨기지 말고 남깁니다.

```markdown
| 2026-06-22 | `make eval` | Failed, then fixed | Eval failed after removing a required phrase from `FAQ-001`; passed after restoring it | Training-only failure rehearsal with synthetic data |
```

### 7. 인수인계 문서 업데이트하기

아래 파일을 확인합니다.

```text
starter-kits/faq-agent-lite/_handoff/handoff.md
```

운영자가 바꾼 내용이 있다면 다음 항목을 최신 상태로 맞춥니다.

- 무엇을 바꿨는지
- 어떤 명령을 실행했는지
- 통과한 검증은 무엇인지
- 아직 실제 운영에 쓰면 안 되는 이유는 무엇인지
- 다음 담당자가 누구인지 또는 어떤 역할인지

예시 문장:

```text
2026-06-22에 `FAQ-001`의 합성 답변 문구를 운영자 교육용으로 일부 수정했다.
`make eval`과 `make validate`를 실행했고 통과했다.
실제 보험 약관, 고객 데이터, 내부 시스템 정보는 사용하지 않았다.
```

## 실패했을 때 대응표

| 상황 | 보이는 증상 | 먼저 확인할 것 | 운영자 대응 |
|---|---|---|---|
| 잘못된 폴더에 있음 | `make: *** No rule to make target 'demo'` 또는 `README.md`가 안 보임 | `pwd`, `ls` | `codex-agent-fieldkit` repo root로 이동한 뒤 다시 실행합니다. |
| `make`가 없음 | `command not found: make` | Mac 또는 개발 환경에 command line tools가 있는지 | Codex에게 "`make` 없이 같은 검증을 실행하는 명령을 알려 달라"고 요청하고, 설치가 필요한 경우 기술 담당자에게 넘깁니다. |
| Python이 없음 | `python3: command not found` | `python3 --version` | Python 3 설치가 필요합니다. 설치 전에는 데이터를 수정하지 말고 환경 준비 상태를 handoff에 남깁니다. |
| eval 점수가 기준보다 낮음 | `Eval score below threshold` | 어떤 케이스가 `FAIL`인지 | 실패한 `G001` 같은 케이스를 보고 CSV 답변과 `tests/golden_set.jsonl`의 기대 문구가 맞는지 확인합니다. 실제 데이터로 보강하지 말고 합성 예시로 수정합니다. |
| private-term scan 실패 | `check_no_private_terms` 또는 안전 스캔 실패 | 새로 넣은 회사명, 내부 링크, 사람 이름, 고객 정보 | 공개 가능한 가상명으로 바꿉니다. 예: 실제 회사명 대신 `ACME Life`, 실제 고객명 대신 `Sample Customer`. |
| validation log를 안 고침 | 검증은 했지만 기록이 없음 | `starter-kits/faq-agent-lite/docs/validation_log.md` | 실행한 명령, 결과, 증거, 남은 한계를 한 줄 추가합니다. 기록이 없으면 다음 사람이 상태를 믿을 수 없습니다. |
| handoff가 오래됨 | 검증 결과와 인수인계 문서 내용이 다름 | `_handoff/handoff.md` | 최신 실행 결과와 남은 위험을 맞춥니다. "검증 완료"라고 쓰려면 실제 명령 결과가 있어야 합니다. |

## 운영자 완료 기준

아래를 모두 만족해야 이 15-30분 루프가 끝난 것입니다.

- 올바른 repo root에서 실행했다.
- Codex가 먼저 구조를 점검했고, 바로 수정부터 하지 않았다.
- `make demo`를 실행했다.
- `sample_faqs.csv`의 합성 FAQ 한 줄을 수정했다.
- `make eval` 또는 `make validate` 결과를 확인했다.
- 실패가 있었다면 원인과 수정 내용을 기록했다.
- `docs/validation_log.md`를 최신화했다.
- `_handoff/handoff.md`에 다음 담당자가 알아야 할 상태를 남겼다.
- 실제 고객 데이터, 내부 링크, 비공개 보험 자료를 넣지 않았다.

이 가이드는 운영 연습용입니다. 실제 보험 상담, 약관 안내, 청구 심사, 민원 답변에
사용하려면 별도의 데이터 승인, 법무/준법 검토, 개인정보 검토, 운영 책임자 승인이
필요합니다.
