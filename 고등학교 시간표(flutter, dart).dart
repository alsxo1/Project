import 'package:flutter/material.dart'; // Flutter 패키지 가져오기

void main() {
  runApp(MyApp()); // 앱 실행
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '고등학교 시간표', // 앱 타이틀 설정
      theme: ThemeData(
        primarySwatch: Colors.blue, // 기본 테마 색상 설정
      ),
      home: TimetablePage(), // 메인 페이지로 TimetablePage 설정
    );
  }
}

class TimetablePage extends StatefulWidget {
  @override
  _TimetablePageState createState() => _TimetablePageState(); // 상태 관리 클래스 생성
}

class _TimetablePageState extends State<TimetablePage> {
  List<List<String>> timetable = List.generate(8, (i) => List.generate(6, (j) => '')); // 8x6 배열 생성, 각 셀의 수업 내용 저장

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('고등학교 시간표'), // 앱바 타이틀 설정
      ),
      body: Column(
        children: <Widget>[
          _buildHeaderRow(), // 상단 헤더 생성
          Expanded(
            child: _buildTimetable(), // 시간표 생성
          ),
        ],
      ),
    );
  }

  // 상단 헤더 행 생성
  Widget _buildHeaderRow() {
    return Row(
      children: <Widget>[
        _buildHeaderCell(''), // 빈 셀 (첫 번째 열)
        _buildHeaderCell('월'), // 월요일
        _buildHeaderCell('화'), // 화요일
        _buildHeaderCell('수'), // 수요일
        _buildHeaderCell('목'), // 목요일
        _buildHeaderCell('금'), // 금요일
      ],
    );
  }

  // 헤더 셀 생성
  Widget _buildHeaderCell(String label) {
    return Expanded(
      child: Container(
        padding: EdgeInsets.all(8.0),
        color: Colors.grey[300], // 셀 배경색 설정
        child: Center(child: Text(label, style: TextStyle(fontWeight: FontWeight.bold))), // 셀 텍스트 설정
      ),
    );
  }

  // 시간표 생성
  Widget _buildTimetable() {
    return GridView.builder(
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 6), // 6열 그리드 설정
      itemCount: 8 * 6, // 총 48개의 셀 생성 (8행 x 6열)
      itemBuilder: (context, index) {
        int row = index ~/ 6; // 행 계산
        int col = index % 6; // 열 계산

        if (col == 0) { // 첫 번째 열 (교시 표시)
          return Container(
            padding: EdgeInsets.all(8.0),
            color: Colors.grey[300], // 셀 배경색 설정
            child: Center(child: Text('${row + 1}교시', style: TextStyle(fontWeight: FontWeight.bold))), // 교시 텍스트 설정
          );
        } else { // 나머지 셀 (수업 내용)
          return GestureDetector(
            onTap: () {
              _editCell(row, col - 1); // 셀을 터치하면 _editCell 호출
            },
            child: Container(
              margin: EdgeInsets.all(1.0),
              color: Colors.white, // 셀 배경색 설정
              child: Center(child: Text(timetable[row][col - 1])), // 셀 내용 표시
            ),
          );
        }
      },
    );
  }

  // 셀 수정 기능
  void _editCell(int row, int col) {
    TextEditingController controller = TextEditingController(text: timetable[row][col]); // 현재 셀 내용으로 초기화된 텍스트 컨트롤러 생성

    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text('수업 내용 입력'), // 다이얼로그 타이틀
          content: TextField(
            controller: controller,
            decoration: InputDecoration(hintText: '수업 내용을 입력하세요'), // 텍스트 필드 힌트 설정
          ),
          actions: <Widget>[
            TextButton(
              child: Text('취소'), // 취소 버튼
              onPressed: () {
                Navigator.of(context).pop(); // 다이얼로그 닫기
              },
            ),
            TextButton(
              child: Text('저장'), // 저장 버튼
              onPressed: () {
                setState(() {
                  timetable[row][col] = controller.text; // 셀 내용 업데이트
                });
                Navigator.of(context).pop(); // 다이얼로그 닫기
              },
            ),
          ],
        );
      },
    );
  }
}
