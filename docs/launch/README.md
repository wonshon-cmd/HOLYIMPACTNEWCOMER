# Tend by name — 런칭 체크리스트 (지금 하는 순서대로)

> 법률·세무 자문이 아니에요. 금액과 절차는 바뀔 수 있으니 각 단계의 공식 사이트에서 마지막으로 확인하세요.
> 실제 신청은 본인 명의로 직접 해야 해요. 여기 있는 건 바로 붙여 넣을 수 있게 준비한 답과 파일이에요.

준비된 파일
- 웹사이트: `site/index.html`, 배포 설정 `.github/workflows/pages.yml`
- 상표 출원용 로고 JPG (흑백, 944px 이하): `docs/launch/uspto/`
- 상표 출원서에 붙여 넣을 답: `docs/launch/trademark-application.md`
- 디자인 특허용 화면 참고 이미지: `docs/launch/design-figures/`
- 저장소 저작권 고지: `/LICENSE`

---

## STEP 0. 오늘 먼저: 저장소 공개 여부 결정 (5분)

지금 이 GitHub 저장소는 **공개(public)** 상태예요. 누구나 코드, 화면 디자인, 로고를 볼 수 있어요.

- 디자인과 만드는 방법을 지키려면 **비공개(private)로 바꾸는 걸 추천**해요.
  GitHub → 저장소 → Settings → 맨 아래 Danger Zone → Change visibility → Make private
- 단, 무료 GitHub Pages는 공개 저장소에서만 돼요. 비공개로 바꾸면 웹사이트는 STEP 1의 방법 B로 올려요.
- 참고: 오늘(2026-11-22) 데모 화면이 공개 저장소에 올라갔어요. 미국 디자인 특허는 본인이 처음 공개한 날로부터 1년 안에 출원하면 돼요(STEP 7).

## STEP 1. 웹사이트 올리기 (15분)

**방법 A — GitHub Pages (저장소를 공개로 둘 때)**
1. 이 작업 브랜치(`claude/magical-bohr-ga9qcs`)를 `main`에 합쳐요. GitHub에서 Pull request를 만들고 Merge.
2. 저장소 → Settings → Pages → Build and deployment → Source를 **GitHub Actions**로.
3. Actions 탭에서 "Deploy website"가 초록색이 되면 끝. 주소: `https://wonshon-cmd.github.io/HOLYIMPACTNEWCOMER/`

**방법 B — Cloudflare Pages 또는 Netlify (저장소를 비공개로 둘 때, 무료)**
1. Cloudflare Pages(또는 Netlify) 가입 → GitHub 연결 → 이 저장소 선택
2. Build command: 비움 / Output(Publish) directory: `site`
3. Deploy. `xxxx.pages.dev` 같은 주소가 바로 나와요.

**도메인 연결 (도메인을 산 뒤)**
- 고른 도메인을 사서, Pages 설정의 Custom domain에 입력하고 도메인 회사에서 안내하는 DNS 값을 넣으면 돼요.

## STEP 2. 이름 확인 (30분) — LLC와 상표 전에 꼭

1. **USPTO 상표 검색**: https://tmsearch.uspto.gov
   - "TEND BY NAME", "TEND"를 검색하고 Class 009, 042에서 비슷한 소프트웨어 상표가 있는지 봐요.
   - "TEND"만 쓰는 다른 분야 회사(예: 치과 브랜드 등)는 있을 수 있어요. 그래서 상표는 **TEND BY NAME** 전체로 내는 게 안전해요.
2. **뉴저지 사업자 이름 검색**: NJ Business Records Service(https://www.njportal.com/DOR/BusinessNameSearch)에서 "Tend by name" 확인.

## STEP 3. 뉴저지 LLC 만들기 (30분, 온라인)

사이트: https://www.njportal.com/DOR/BusinessFormation → Limited Liability Company (Domestic)

준비할 답
- 회사 이름: **Tend by name LLC**
- 사업 목적: Software for churches and religious organizations
- Registered Agent: 본인(뉴저지 주소 필요) 또는 등록대행 회사
- 주된 사업장 주소, 대표(Member/Manager) 이름과 주소
- 수수료: 약 $125 (신청 화면에서 확인)

끝나면
- Certificate of Formation(설립 증명) PDF를 저장해요.
- 이어서 **NJ-REG**(주 세금 등록)을 온라인으로 해요. https://www.njportal.com/njbgs/
- 매년 연례 보고(Annual Report)가 있어요. 약 $75.

## STEP 4. EIN 받기 (15분, 무료, 바로 발급)

사이트: IRS "Apply for an Employer Identification Number (EIN) Online" (irs.gov) — 월–금 동부시간 오전 7시–오후 10시

준비할 답
- Type: Limited Liability Company
- Members: 1명이면 1
- State: New Jersey
- Reason: Started a new business
- Responsible party: 본인 이름 + SSN 또는 ITIN
- 사업 시작일: LLC 설립일

끝나면 확인서(EIN Confirmation Letter, CP 575) PDF를 **그 자리에서 꼭 저장**하세요. 다시 받기 번거로워요.

## STEP 5. 사업용 은행 계좌 (30분)

Certificate of Formation + EIN 확인서 + 신분증을 들고 은행에서 Business checking 개설. 회사 돈과 개인 돈을 나눠야 LLC 보호가 유지돼요.

## STEP 6. 상표 출원 — USPTO (1시간)

1. USPTO.gov 계정 만들기 + 본인 인증(ID.me)
2. **Trademark Center**(https://www.uspto.gov/trademarks/apply)에서 새 출원
3. `docs/launch/trademark-application.md`의 답을 그대로 붙여 넣어요.
4. 추천 순서
   - **1순위: 글자 상표 "TEND BY NAME" (Standard characters)** — 어떤 글꼴로 써도 보호돼요. 가장 중요해요.
   - 2순위: 로고 상표 (Special form) — `docs/launch/uspto/tendbyname-logo-horizontal.jpg`
5. 수수료: 2025년 기준 Class 하나당 약 $350 (Class 9, 42 두 개면 약 $700). 신청 화면에서 확인.
6. 출원 후 심사까지 보통 1년 안팎. 등록 전에는 **™**, 등록 후에는 **®**를 써요.

## STEP 7. 디자인 보호

**(1) 디자인 특허 — 화면 디자인 자체를 보호 (가장 강력)**
- USPTO Patent Center에서 "Design" 출원. 제목 예: *Display screen or portion thereof with graphical user interface*
- 출원 하나에 디자인 하나. 추천 화면 3개 (`docs/launch/design-figures/`):
  1. `fig1-leader-seating.png` — 순장 테이블 배치 화면 (내 자리가 아래, 카드형 새가족 정보)
  2. `fig3-phone-welcome-name.png` — 한 화면에 질문 하나, 밀어서 다음으로 가는 등록 화면
  3. `fig4-phone-checkin-name-match.png` — 이름을 쓰면 가려진 번호와 함께 찾아주는 체크인
- 이 PNG는 참고용이에요. 정식 출원에는 **흑백 선 도면**(보호할 부분은 실선, 아닌 부분은 점선)이 필요해요. 특허 도면 전문가나 특허 변리사(Patent agent/attorney)에게 맡기는 걸 강력히 추천해요.
- 수수료는 Micro/Small entity 할인 여부에 따라 크게 달라요. USPTO Fee schedule에서 확인.
- 기한: 처음 공개한 날(데모 공개: 2026-11-22)로부터 **1년 안**. 한국 등 다른 나라에도 낼 생각이면 더 빨리 내는 게 안전해요.

**(2) 저작권 등록 — 코드, 웹사이트 글과 그래픽 (저렴, 온라인)**
- https://www.copyright.gov/registration → eCO
- 따로 두 건 추천
  1. Computer program: Tend by name 소프트웨어 (소스 코드 앞뒤 일부 제출, 영업비밀은 가릴 수 있어요)
  2. Website text and artwork: Tend by name 웹사이트
- 수수료: Standard Application 약 $65 (건당). 등록은 저작권 침해 소송의 전제 조건이에요.
- 참고: 단순한 글자 로고는 저작권보다 **상표**로 보호하는 게 맞아요.

**(3) 영업비밀과 계약**
- 저장소 비공개 (STEP 0)
- 함께 일하는 사람에게 NDA(비밀유지계약) 받기
- 교회 고객과는 이용약관(Terms of Service)을 맺기

## STEP 8. 실제 교회 데이터를 받기 전에 꼭

새가족의 이름, 전화번호, 생년월일, 주소는 개인정보예요. 실제로 쓰기 전에
- 개인정보처리방침(Privacy Policy)과 이용약관(Terms of Service)을 웹사이트에 올리고
- 데이터는 이 데모처럼 브라우저가 아니라 안전한 서버 데이터베이스에 저장해야 해요.

## (선택) 한국에도 낼 때
- 한국 교회 대상이면 특허로(https://www.patent.go.kr)에서 상표·디자인 출원 가능.

---

### 오늘 할 일 요약
1. 저장소 공개/비공개 결정 → 웹사이트 올리기 (STEP 0–1)
2. 이름 검색 (STEP 2)
3. LLC → EIN → 은행 (STEP 3–5)
4. 상표 "TEND BY NAME" 출원 (STEP 6)
5. 디자인 특허는 변리사 상담 예약, 저작권은 eCO로 직접 (STEP 7)
