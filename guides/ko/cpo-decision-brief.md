# CPO Decision Brief

## 한 줄 판단

Codex Agent Fieldkit은 비개발자가 agent demo를 prompt 문서가 아니라
검증 가능한 폴더, eval, safety scan, validation log, handoff로 남기게 하는
공개 안전 학습 키트입니다.

## 언제 쓰나

- 팀에 agent 데모는 있지만 검증과 인수인계 방식이 없을 때
- PM/운영자가 Codex로 작은 agent를 만들고 개발 리뷰에 넘겨야 할 때
- 기업 AI 교육을 prompt literacy에서 delivery literacy로 올리고 싶을 때

## 기대 결과

- 60분 안에 synthetic FAQ agent를 실행한다.
- golden-set eval과 unit test를 본다.
- safety scan과 validation report를 생성한다.
- handoff 문서로 다음 담당자에게 넘긴다.

## 쓰면 안 되는 경우

- 실제 고객 상담 자동화에 바로 연결하려는 경우
- 실제 약관, 청구 기록, 고객 데이터를 넣으려는 경우
- production certification을 기대하는 경우

## 승인 라인

| 역할 | 확인할 것 |
|---|---|
| Business owner | 어떤 업무를 줄이고 싶은가 |
| Data owner | 어떤 데이터가 허용되는가 |
| Compliance/privacy | 어떤 질문은 반드시 멈춰야 하는가 |
| Technical maintainer | 누가 운영, 배포, 장애 대응을 맡는가 |
| Support owner | 실패하면 누가 사용자와 현장을 돕는가 |

## 다음 결정

1. 공개 fieldkit으로 60분 워크숍을 먼저 돌린다.
2. 사내 업무 후보 1개를 synthetic data로 다시 쓴다.
3. private adaptation은 별도 repo에서 승인 라인을 두고 진행한다.
