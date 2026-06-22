# PM 리더를 위한 Codex Agent Fieldkit 가이드

이 레포는 프롬프트 모음이 아닙니다.

비개발자가 Codex로 AI agent를 만들 때 필요한 작업면을 제공합니다.

```text
아이디어 -> 폴더 구조 -> AGENTS.md -> starter agent -> 테스트 -> eval -> release scan -> handoff
```

## 왜 PM에게 중요한가

AI agent 프로젝트는 데모가 되는 순간보다, 다음 질문에 답할 수 있을 때 진짜 진전됩니다.

- 무엇을 만들었는가?
- 어떤 데이터로 만들었는가?
- 어떤 질문에는 맞고 어떤 질문에는 못 맞는가?
- 실패하면 누가 고치는가?
- 공개해도 안전한가?
- 다음 담당자에게 무엇을 넘겨야 하는가?

이 레포는 그 질문을 파일과 명령어로 바꿉니다.

## PM이 봐야 할 파일

| 목적 | 파일 |
|---|---|
| 전체 구조 | `README.md` |
| 시작 순서 | `START_HERE.md` |
| 요구사항 | `starter-kits/faq-agent-lite/docs/prd.md` |
| 구조 | `starter-kits/faq-agent-lite/docs/architecture.md` |
| 검증 증거 | `starter-kits/faq-agent-lite/docs/validation_log.md` |
| 인수인계 | `starter-kits/faq-agent-lite/_handoff/handoff.md` |
| 공개 안전성 | `docs/public-first-safety/` |

## PM의 완료 기준

완료는 "데모가 한 번 됐다"가 아닙니다.

완료 기준:

- `make demo`가 동작한다.
- `make test`가 통과한다.
- `make eval`이 기준 점수 이상이다.
- `make validate`가 통과한다.
- validation log가 최신이다.
- handoff에 한계와 다음 소유자가 적혀 있다.

## 리더가 확인할 질문

1. 실제 고객 데이터가 들어갔는가?
2. golden set이 중요한 사용자 질문을 포함하는가?
3. fallback이 안전하게 설계되어 있는가?
4. 배포 전 필요한 승인자는 누구인가?
5. 이 결과를 다른 팀원이 재현할 수 있는가?

## 링크드인/사내 공유 포지셔닝

이 레포는 "Codex로 agent를 만드는 법"보다 좁고 실용적인 메시지를 갖습니다.

```text
비개발자가 AI agent를 만들 때 필요한 것은 더 좋은 프롬프트가 아니라,
검증 가능한 작업 구조와 안전한 인수인계 체계다.
```
