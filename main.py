# استيراد البيانات من الملف اللي عملته
from bacteria_data import bacteria_db, tests, test_names


def get_user_input():
    """دالة لأخذ نتائج الاختبارات من المستخدم"""
    print( "🔬 ادخل نتائج الاختبارات:" )
    print( "الخيارات المتاحة: +ve, -ve, variable" )
    print( "-" * 50 )

    user_results = {}

    for test in tests:
        while True:
            result = input( f"{test_names[test]}: " ).strip().lower()

            # تحويل الإجابات لنفس الصيغة
            if result in ["+ve", "positive", "pos", "+", "موجب"]:
                user_results[test] = "+ve"
                break
            elif result in ["-ve", "negative", "neg", "-", "سالب"]:
                user_results[test] = "-ve"
                break
            elif result in ["variable", "var", "متغير", "v"]:
                user_results[test] = "variable"
                break
            else:
                print( "❌ إجابة غير صحيحة! اكتب: +ve أو -ve أو variable" )

    return user_results


def calculate_match_percentage(user_results, bacteria_profile):
    """حساب نسبة التطابق بين نتائج المستخدم وبروفايل البكتيريا"""
    matches = 0
    total_tests = len( tests )

    for test in tests:
        user_result = user_results[test]
        bacteria_result = bacteria_profile[test]

        # إذا البكتيريا متغيرة في الاختبار ده، تعتبر مطابقة
        if bacteria_result == "variable" or user_result == bacteria_result:
            matches += 1

    return (matches / total_tests) * 100


def identify_bacteria(user_results):
    """تحديد البكتيريا الأقرب للنتائج"""
    matches = []

    for bacteria_name, bacteria_profile in bacteria_db.items():
        match_percentage = calculate_match_percentage( user_results, bacteria_profile )
        matches.append( {
            'name': bacteria_name,
            'percentage': match_percentage,
            'profile': bacteria_profile
        } )

    # ترتيب النتائج من الأعلى للأقل
    matches.sort( key=lambda x: x['percentage'], reverse=True )

    return matches


def display_results(matches):
    """عرض النتائج للمستخدم"""
    print( "\n" + "=" * 60 )
    print( "🎯 نتائج التحليل:" )
    print( "=" * 60 )

    if matches[0]['percentage'] == 0:
        print( "❌ لم يتم العثور على تطابق مناسب" )
        print( "تأكد من صحة النتائج المدخلة" )
        return

    # عرض أفضل 5 نتائج
    for i, match in enumerate( matches[:5], 1 ):
        percentage = match['percentage']
        name = match['name']

        if i == 1:
            print( f"🏆 الأكثر احتمالاً: {name}" )
            print( f"   نسبة التطابق: {percentage:.1f}%" )

            if percentage == 100:
                print( "   ✅ تطابق كامل!" )
            elif percentage >= 80:
                print( "   ✅ تطابق عالي" )
            elif percentage >= 60:
                print( "   ⚠️ تطابق متوسط" )
            else:
                print( "   ❓ تطابق ضعيف" )
        else:
            print( f"{i}. {name}: {percentage:.1f}%" )

        print()


def show_comparison(user_results, bacteria_name):
    """عرض مقارنة تفصيلية بين نتائج المستخدم والبكتيريا المحددة"""
    if bacteria_name not in bacteria_db:
        print( "❌ اسم البكتيريا غير موجود" )
        return

    bacteria_profile = bacteria_db[bacteria_name]

    print( f"\n📊 مقارنة تفصيلية مع {bacteria_name}:" )
    print( "-" * 50 )

    for test in tests:
        user_result = user_results[test]
        bacteria_result = bacteria_profile[test]

        match_symbol = "✅" if (bacteria_result == "variable" or user_result == bacteria_result) else "❌"

        print(
            f"{test_names[test]:<25} | المدخل: {user_result:<8} | {bacteria_name}: {bacteria_result:<8} {match_symbol}" )


def main():
    """الدالة الرئيسية للبرنامج"""
    print( "🔬" + "=" * 50 + "🔬" )
    print( "       برنامج تحديد البكتيريا" )
    print( "🔬" + "=" * 50 + "🔬" )
    print()

    while True:
        try:
            # أخذ النتائج من المستخدم
            user_results = get_user_input()

            # تحديد البكتيريا
            matches = identify_bacteria( user_results )

            # عرض النتائج
            display_results( matches )

            # سؤال المستخدم إذا كان يريد مقارنة تفصيلية
            if matches[0]['percentage'] > 0:
                show_detailed = input( "هل تريد مقارنة تفصيلية مع أفضل نتيجة؟ (y/n): " ).strip().lower()
                if show_detailed in ['y', 'yes', 'نعم', 'ن']:
                    show_comparison( user_results, matches[0]['name'] )

            # سؤال عن إعادة التشغيل
            print( "\n" + "-" * 50 )
            restart = input( "هل تريد تجربة عينة أخرى؟ (y/n): " ).strip().lower()
            if restart not in ['y', 'yes', 'نعم', 'ن']:
                break

            print( "\n" )

        except KeyboardInterrupt:
            print( "\n\n👋 تم إنهاء البرنامج" )
            break
        except Exception as e:
            print( f"❌ حدث خطأ: {e}" )


if __name__ == "__main__":
    main()