#include <QCoreApplication>
#include <QDebug>

int main(int argc, char *argv[])
{
    QCoreApplication app(argc, argv);

    if (argc < 2) {
        qWarning() << "No file path provided";
        return 1;
    }

    QString filePath = argv[1];
    qDebug() << "Processing file:" << filePath;

    return 0;
}